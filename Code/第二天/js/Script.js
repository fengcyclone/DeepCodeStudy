var btn01 = document.getElementById("button1");
btn01.onclick = function (){
    var answer = 1 ;
    for(var i = 2 ; i <= 66 ; i++){
        answer *= i ;
    }
    alert(answer);
}

var btn02 = document.getElementById("button2");
btn02.onclick = function () {
    var num = document.getElementById("homework2_input").value;
    num = Number(num)
    if (num % 2 == 0) {
        alert("请输入奇数，否则三角没有角")
    }
    else {
            var answer = '';
            for (var i = 0; i < num; i++) {
                for (var j = 0; j < num; j++) {
                    if (j - i >= 0 && num - j > i) {
                        answer += '$';
                    }
                    else {
                        answer += '  ';
                    }
                }
                answer += "\n";
            }
            alert(answer);
    }
}

var btn03 = document.getElementById("button3");
btn03.onclick = function(){
    var num = document.getElementById("homework3_input").value;
    num = Number(num);
    var answer = 1;
    for(var i = num ; i > 1 ; i--)
    {
        answer *= i;
    }
    alert(answer) ;
}