from django.urls import path

from . import views


"""
# 1st arg is url
# 2nd arg is function name
# 3rd arg is alis name for url
"""
urlpatterns = [
    path('ex1/', views.ex1,name="ex1 page"),
    path('hello/', views.handleHello,name="ex2 page"),
    path('process/', views.process, name="process page"),
    path('responseData/', views.handleResponseData,name=" page"),
    path('responseMultiData/', views.handleMultipleResponse,name="ex1 page"),
    path('show1/', views.handleShow1, name="show1-page"),
    path('show2/', views.handleShow2, name="show2-page"),
    path('show3/', views.handleShow3, name="show3 page"),
    path('show4/', views.handleShow4, name="show4 page"),
    path('show5/', views.handleShow5, name="show5 page"),
    path('show6/', views.handleShow6, name="show6 page"),
    path('', views.handleIndex,name="index page"),
    path('show7/', views.handleIf, name="IF-page"),
    path('request1/', views.handleRequest1, name="request1-page"),
    path('submit1/', views.handleSubmit1, name="submit1 page"),

    path('requestPost/', views.handlePostRequest, name="requestPost-page"),
    path('submitPost/', views.handleSubmitPost, name="submitPost-page"),

    path('requestGetAndPost/', views.showRequestGetAndPost, name="requestPost-page"),
    path('submitRequestGetAndPost/', views.handleRequestGetAndPost, name="requestPost-page"),

    path('request2/', views.handleRequest2, name="request2 page"),
    path('submit2/', views.handleSubmit2, name="request2 page"),

    path('showLogin/', views.showLogin, name="login-page"),
    path('submitLogin/', views.handleLogin, name="submit-Login"),

    path('register/', views.handleRegister, name="register-page"),
    path('register2/', views.handleRegister2, name="register2-page"),

    path('reuse/', views.handleReuse, name="reuse page"),

    path('form1/', views.handleForm1, name="form1-page"),
    path('processForm1/', views.handleForm2, name="ex2 page"),

    path('pdf/', views.getpdf, name="pdf-page"),
    path('csv/', views.getCsv, name="csv-page"),

    path('setcookie/', views.handleSetCookie, name="setcookie-page"),
    path('getcookie/', views.handleGetCookie, name="getcookie-page"),
    path('deletecookie/', views.handleDeleteCookie, name="deletecookie-page"),


    path('person/', views.handlePerson, name="person-page"),#using model form
    path('onetoone/', views.handleOnetoone, name="onetoone-page"),
    path('manytoone/', views.handleManytoone, name="manytoone-page"),
    path('manytomany/', views.handleManytomany, name="manytomany-page"),

    path('css/', views.handleCss, name="css-page"),
    path('reuse1/', views.handleReuse1, name="reuse1"),
    path('reuse2/', views.handleReuse2, name="reuse2"),
]
