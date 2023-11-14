let switchFrm = document.querySelector('#switch-form')
let switchF1 = document.querySelector('#switch-f1')
let switchF2 = document.querySelector('#switch-f2')
let switchCircle = document.querySelectorAll('.switch-circle')
let switchBtn = document.querySelectorAll('.switch-btn')
let regFrm=document.querySelector('#register-form')
let logFrm=document.querySelector('#login-form')
let allButtons=document.querySelectorAll('.submit')

let getButtons = (e) => e.preventDefault()

let changeForm=(e) =>{
    switchFrm.classList.add('is-gx')
    setTimeout(function(){
        switchFrm.classList.remove('is-gx')
    },1500)
    switchFrm.classList.toggle('is-txr')
    switchCircle[0].classList.toggle('is-txr')
    switchCircle[1].classList.toggle('is-txr')

    switchF1.classList.toggle('is-hidden')
    switchF2.classList.toggle('is-hidden')
    regFrm.classList.toggle('is-txl')
    logFrm.classList.toggle('is-txl')
    logFrm.classList.toggle('is-z200')
}

let mainF = (e) => {
    for(var i = 0; i < allButtons.length; i++){
        allButtons[i].addEventListener('click',getButtons)
    }
    for(var i = 0; i < switchBtn.length; i++){
        switchBtn[i].addEventListener('click',changeForm)   
    }
}

function login(){
    var id = document.querySelector('#id');
    var pw = document.querySelector('#pw');

    if(id.value == id.value||pw.value==pw.value){
        location.href='/Users/jangbyeongjun/code/산프 관리자 페이지/admin_page.html';
    }
    else{
        alert("로그인 되었씁니다 !")
        location.href='/Users/jangbyeongjun/code/산프 관리자 페이지/admin_page.html';
    }
}

function back(){
    history.go(-1);
}

function create_id(){
    var id = document.querySelector('#id');
    var pw = document.querySelector('#pw');
    var a_pw = document.querySelector('#a_pw');
    if(id.value==""||pw.value==""||a_pw.value==""){
        alert("cant account")
    }
    else{
        if(pw.value!==a_pw.value){
            alert("cant account")
        }
        else{
            alert("회원가입 되었습니다 !")
        }
    }
}

function move_login(){
    window.location.href = "{% url 'login' %}";
}

function move_register() {
    window.location.href = "register.html";
//    window.location.href = "http://127.0.0.1:3000/capstoneDesign/register.html";
}

function toggleSocialButtons() {
    var socialButtons = document.getElementById('social-buttons');
    if (socialButtons.style.display === 'none') {
        socialButtons.style.display = 'block';
    } else {
        socialButtons.style.display = 'none';
    }
}

function naver_login() {
    window.location.href = "naver.com";
    // Perform action for Naver login
}

function kakao_login() {
    window.location.href = "google.com";
    // Perform action for KakaoTalk login
}



window.addEventListener('load',mainF)