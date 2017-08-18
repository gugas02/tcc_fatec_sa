from flask import Flask, render_template, request , flash, redirect, url_for, jsonify,send_from_directory
from flask_login import LoginManager, login_user,logout_user,login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from model.forms import LoginForm
import time

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["use_reloader"]=False

app.config["SECRET_KEY"] = "uma-senha-mto-segura"

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="gugas02",
    password="Rasp13erryP1",
    hostname="gugas02.mysql.pythonanywhere-services.com",
    databasename="gugas02$compartilhaCan",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config['UPLOAD_FOLDER'] = 'uploads/'

db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(64), unique=True)
    nome = db.Column(db.String(80))
    dataNascimento = db.Column(db.String(10))
    marcaCarro = db.Column(db.String(80))
    modeloCarro = db.Column(db.String(120))
    anoCarro = db.Column(db.String(10))
    anoFab = db.Column(db.String(10))
    senha = db.Column(db.String(80))

    @property
    def is_authenticated(self):
        return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, username, email,nome,dataNascimento,marcaCarro,modeloCarro,anoCarro,anoFab,senha):
        self.username = username
        self.email = email
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.marcaCarro = marcaCarro
        self.modeloCarro = modeloCarro
        self.anoCarro = anoCarro
        self.anoFab = anoFab
        self.senha = senha

    def __repr__(self):
        return '<User %r>' % self.username


class UserCar(db.Model):
    __tablename__ = "dataCar"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    consumoMedio = db.Column(db.String(64))
    pressaoTurbo = db.Column(db.String(80))
    tempAgua = db.Column(db.String(10))
    pressaoColetor = db.Column(db.String(80))
    tempAdm = db.Column(db.String(120))
    pontoIgn = db.Column(db.String(10))
    fluxoAr = db.Column(db.String(10))
    nvlCombustivel = db.Column(db.String(80))
    dtc = db.Column(db.String(80))
    tempOleo = db.Column(db.String(80))
    relacaoEstequiometrica = db.Column(db.String(80))
    consumoInstantaneo = db.Column(db.String(80))
    marchaNConforme = db.Column(db.String(80))

    user = db.relationship('User', foreign_keys= user_id)

    def __init__(self,user_id, consumoMedio,pressaoTurbo,tempAgua,pressaoColetor,tempAdm,pontoIgn,fluxoAr,nvlCombustivel,dtc,tempOleo,relacaoEstequiometrica,consumoInstantaneo,marchaNConforme):
        self.user_id = user_id
        self.consumoMedio = consumoMedio
        self.pressaoTurbo = pressaoTurbo
        self.tempAgua = tempAgua
        self.pressaoColetor = pressaoColetor
        self.tempAdm = tempAdm
        self.pontoIgn = pontoIgn
        self.fluxoAr = fluxoAr
        self.nvlCombustivel = nvlCombustivel
        self.dtc = dtc
        self.tempOleo = tempOleo
        self.relacaoEstequiometrica = relacaoEstequiometrica
        self.consumoInstantaneo = consumoInstantaneo
        self.marchaNConforme = marchaNConforme

    def __repr__(self):
       return '<UserCar %r>' % self.id

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id = id).first()

@app.route("/")
def index():
    return render_template("main_page.html")



@app.route("/mycalculator",methods=["GET", "POST"])
def mycalculator():
    if request.method == 'GET':
        return render_template("mycalculator.html")

    elif request.method == 'POST':
        expression = request.form.get('expression')
        result = eval(expression)
        return render_template("resultado.html", result=result)


@app.route("/apiUi",methods=["GET", "POST"])
def apiUi():
    if request.method == 'GET':
        return render_template("apiUi.html")

    elif request.method == 'POST':
        user_id = request.form.get('user_id')
        consumoMedio = request.form.get('consumoMedio')
        pressaoTurbo = request.form.get('pressaoTurbo')
        tempAgua = request.form.get('tempAgua')
        pressaoColetor = request.form.get('pressaoColetor')
        tempAdm = request.form.get('tempAdm')
        pontoIgn = request.form.get('pontoIgn')
        fluxoAr = request.form.get('fluxoAr')
        nvlCombustivel = request.form.get('nvlCombustivel')
        dtc = request.form.get('dtc')
        tempOleo = request.form.get('tempOleo')
        relacaoEstequiometrica = request.form.get('relacaoEstequiometrica')
        consumoInstantaneo = request.form.get('consumoInstantaneo')
        marchaNConforme = request.form.get('marchaNConforme')
        i = UserCar(user_id,consumoMedio,pressaoTurbo,tempAgua,pressaoColetor,tempAdm,pontoIgn,fluxoAr,nvlCombustivel,dtc,tempOleo ,relacaoEstequiometrica,consumoInstantaneo,marchaNConforme)
        db.session.add(i)
        db.session.commit()
        return "ok"


@app.route("/registro",methods=["GET", "POST"])
def registro():
    if request.method == 'GET':
        return render_template("registro.html")

    elif request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        nome = request.form.get('nome')
        dataNascimento = request.form.get('dataNascimento')
        marcaCarro = request.form.get('marcaCarro')
        modeloCarro = request.form.get('modeloCarro')
        anoCarro = request.form.get('anoCarro')
        anoFab = request.form.get('anoFab')
        senha = request.form.get('senha')


        dado = User(username,email,nome,dataNascimento,marcaCarro,modeloCarro,anoCarro,anoFab,senha)
        db.session.add(dado)
        db.session.commit()
        return render_template("sucesso.html")

@app.route("/loginapi",methods=["GET", "POST"])
def loginapi():
    if request.method == 'GET':
        return render_template("loginapi.html")

    elif request.method == 'POST':
        user = request.form.get('user')
        senha = request.form.get('senha')
        login = User.query.filter_by(username= user).first()
        if login.senha == senha:
            result = login.id
            return render_template("resultado.html",result = result)
        else:
            return render_template("loginapi.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and user.senha == form.password.data:
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            flash("Login inválido")
    return render_template('form.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("main_page.html")


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/getect")
@login_required
def getect():
    id = current_user.id
    value = UserCar.query.filter_by(user_id = id).all()
    data = []
    for item in value:
        data.append(item.tempAgua)
    return  jsonify(data)

@app.route("/getsensor_map")
@login_required
def getsensor_map():
    id = current_user.id
    value = UserCar.query.filter_by(user_id = id).all()
    data = []
    for item in value:
        data.append(item.pressaoColetor)
    return jsonify(data)

@app.route("/geteat")
@login_required
def geteat():
    id = current_user.id
    value = UserCar.query.filter_by(user_id = id).all()
    data = []
    for item in value:
        data.append(item.tempAdm)
    return jsonify(data)

@app.route("/getip")
@login_required
def getip():
    id = current_user.id
    value = UserCar.query.filter_by(user_id = id).all()
    data = []
    for item in value:
        data.append(item.pontoIgn)
    return jsonify(data)

@app.route("/gethr")
def gethr():
    hr = time.time()
    return  jsonify(hr)

@app.route('/fonts/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory=app.config['UPLOAD_FOLDER'], filename=filename)


@app.route("/lala")
def lala():
    return render_template("testedatepicker.html")







