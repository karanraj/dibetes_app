from flask import Flask
from flask import render_template
from flask import request

app=Flask("dibetes")


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result",methods=["GET"])
def result():
    name=request.args.get("name")
    preg=request.args.get("preg")
    gl=request.args.get("gl")
    bp=request.args.get("bp")
    st=request.args.get("st")
    ins=request.args.get("in")
    bmi=request.args.get("bmi")
    dpf=request.args.get("dpf")
    age=request.args.get("age")
    from keras.models import load_model
    model=load_model("dibetes_model.h5")
    output=model.predict([[int(preg),int(gl),int(bp),int(st),int(ins),float(bmi),float(dpf),int(age)]])
    if round(output[0][0]) == 1:
        return render_template("result.html",cname=name,pregn=preg,glc=gl,bpr=bp,skt=st,insl=ins,BMI=bmi,DPF=dpf,Age=age,color="Red",result="Positive")
    elif round(output[0][0]) == 0:
        return render_template("result.html",cname=name,pregn=preg,glc=gl,bpr=bp,skt=st,insl=ins,BMI=bmi,DPF=dpf,Age=age,color="Green",result="Negative")

app.run(host="0.0.0.0",port=5000)
