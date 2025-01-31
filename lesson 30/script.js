function gethistory() {
    return document.getElementById("history-value").innerText;
}

function displayhistory(num) {
    document.getElementById("history-value").innerText = num;
}

function getoutput() {
    return document.getElementById("output-value").innerText;
}

function displayoutput(num) {
    if(num=="") {
        document.getElementById("output-value").innerText = num;
    }
    else {
        document.getElementById("output-value").innerText = getformattednumber(num);
    }
}

function getformattednumber(num) {
    if(num=="-") {
        return "";
    }

    var a = Number(num);
    var value = a.toLocaleString("en");
    return value;
}

function reversenumberformat(num) {
    return Number(num.replace(/, /g, ''));
}

var operator = document.getElementsByClassName("operator");

for(var i=0; i<operator.length; i++) {
    operator[i].addEventListener("click", function(){
        if(this.id=="clear") {
            displayhistory("");
            displayoutput("")
        }
        else if(this.id=="backspace") {
            var output = reversenumberformat(getoutput()).toString();
        }
    })
}