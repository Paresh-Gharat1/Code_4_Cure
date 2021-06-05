from django.shortcuts import render
import joblib
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def check(request):
    if (request.method == "POST"):
        age = request.POST.get('age')
        cp = request.POST.get('cp')
        trestbps = request.POST.get('trestbps')
        gender = request.POST.get('gender')
        fbs = request.POST.get('fbs')
        restecg = request.POST.get('restecg')
        exang = request.POST.get('exang')
        oldpeak = request.POST.get('oldpeak')
        slope = request.POST.get('slope')
        ca = request.POST.get('ca')
        thal = request.POST.get('thal')
        chol = request.POST.get('chol')
        thalach = request.POST.get('thalach')
        knn = joblib.load("model.pkl")
        sex = -1
        if gender == "Male":
            sex = 1
        else:
            sex = 0
        para = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        ans = knn.predict(para)
        prob = knn.predict_proba(para)
        if ans == 1:
            ans = "There is a high probability that you are suffereing from heart disease! please consult a doctor"
            lis = ['Coronary heart disease', 'Hypertension', 'Cardiac arrest', 'Heart failure', 'Arrhythmia', 'Peripheral artery disease',
                    'Stroke', 'Congenital heart disease', 'Angina pain', 'Aneurysm', 
            ]
            return render(request, "heart/result1.html", {"ans" : ans, 'lis' : lis})
        else:
            ans = "Congrats we have noted that you are not suffering from any disease as per our information but it's still better to consult a doctor for complete details"
            return render(request, 'heart/result1.html', {'ans' : ans})
    
    else:
        return render(request, "heart/heart.html")

@login_required
def consult(request):
    return render(request, "heart/consult.html")