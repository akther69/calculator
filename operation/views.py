from django.shortcuts import render
from django.views.generic import View

# Create your views here.
#addition
#url:localhost:8000/add/
#method:
    #get: a template with addition form
    #post:extract textbox value and perform operation
    
class AdditionView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"addition.html")
    def post(self,request,*args, **kwargs):
        num1=request.POST.get("box1")
        num2=request.POST.get("box2")
        result=int(num1)+int(num2)
        print(result)
        data={"result":result}
        return render(request,"addition.html",data)
    
    
class BmiView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"bmi.html")
    
    def post(self,request,*args, **kwargs):
        height_in_cm=request.POST.get("heightbox")
        weight_in_kg=request.POST.get("weightbox")
        height_in_m=int(height_in_cm)/100
        result=int(weight_in_kg)/height_in_m**2
        data={"result":result}
        return render(request,"bmi.html",data)
    
    
class SubractionView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"subraction.html")
    def post(self,request,*args, **kwargs):
        num1=request.POST.get("box1")
        num2=request.POST.get("box2")
        result=int(num1)-int(num2)
        print(result)
        data={"result":result}
        return render(request,"subraction.html",data)


class MultiplicationView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"multiplication.html")
    def post(self,request,*args, **kwargs):
        num1=request.POST.get("box1")
        num2=request.POST.get("box2")
        result=int(num1)*int(num2)
        print(result)
        data={"result":result}
        return render(request,"multiplication.html",data)
    
    
class DivisionView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"division.html")
    def post(self,request,*args, **kwargs):
        num1=request.POST.get("box1")
        num2=request.POST.get("box2")
        result=int(num1)/int(num2)
        print(result)
        data={"result":result}
        return render(request,"division.html",data)
    
    
class FactorialView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"factorial.html")
    def post(self,request,*args, **kwargs):
        num=request.POST.get("factorialBox")
        num=int(num)
        a=1
        for i in range(1,num+1):
            a*=i
        print(f"fact:{a}")
        data={'fact':a}
        return render(request,"factorial.html",data)
    
    
class CalorieView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"calorie.html")
    def post(self,request,*args, **kwargs):
        
        weight=request.POST.get("weightBox")
        heigth=request.POST.get("heightBox")
        age=request.POST.get("ageBox")
        gender=request.POST.get("genderBox")
        activity_level=request.POST.get("activityBox")
        print(f"h={heigth},w={weight},g={gender},a={activity_level},age={age}")
        
        if gender=="male":
            BMR=int(weight)+6.25*int(heigth)-5*int(age)+5
        else:
            BMR=int(weight)+6.25*int(heigth)-5*int(age)-161
        calorie=BMR*float(activity_level)
        print(calorie)
        data={'calorie':calorie,"bmt":BMR,"height":heigth,"weigth":weight}
        return render(request,"calorie.html",data)
    
    
class EmiView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"emi.html")
    def post(self,request,*args, **kwargs):
        loan=request.POST.get("loanamountBox")
        interest=request.POST.get("interestrateBox")
        tenure=request.POST.get("tenureBox")
        loan=float(loan)
        interest=float(interest)/100/12
        tenure=int(tenure)
        print(f"a={loan},b={interest},c={tenure}")
        a=(1+interest)**tenure
        b=loan*interest*a
        c=(1+interest)**tenure
        d=c-1
        EMI=b/d
        s=EMI*tenure
        total_interest=s-loan
        total_amount=total_interest+loan
        data={"EMI":EMI,"loan":loan,"total_interest":total_interest,"total_amount":total_amount}
        return render(request,"emi.html",data)
    
class IndexView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"index.html")
    
class CalorimeterView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"calorimeter.html")
    def post(self,request,*args, **kwargs):
        weight=request.POST.get("weightBox")
        heigth=request.POST.get("heightBox")
        age=request.POST.get("ageBox")
        gender=request.POST.get("genderBox")
        activity_level=request.POST.get("activityBox")
        weight_status=request.POST.get("weightstatusBox")
        target_weight=request.POST.get("targetweightBox")
        days=request.POST.get("daysBox")
        target_weight=int(target_weight)
        days=int(days)
        print(f"h={heigth},w={weight},g={gender},a={activity_level},age={age},g={weight_status},t={target_weight},d={days}")
        if gender=="male":
            BMR=int(weight)+6.25*int(heigth)-5*int(age)+5
        else:
            BMR=int(weight)+6.25*int(heigth)-5*int(age)-161
        calorie=BMR*float(activity_level)
        data={'calorie':calorie,"bmt":BMR,"height":heigth,"weigth":weight}
        if weight_status=="gain":
            calories_per_kg=7700
            excess_calories=target_weight*calories_per_kg
            daily_excess_calorie=excess_calories/days
            total_daily_calorie_intake=calorie+daily_excess_calorie
        elif weight_status=="loss":
            calories_per_kg=7700
            excess_calories=target_weight*calories_per_kg
            daily_excess_calorie=excess_calories/days
            total_daily_calorie_intake=calorie-daily_excess_calorie
        data={"daily_intake":total_daily_calorie_intake,"calorie":calorie}
        return render(request,"calorimeter.html",data)