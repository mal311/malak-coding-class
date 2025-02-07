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

            if(output) { //if the output has a value
                output = output.substring(0, output.length-1);
                displayoutput(output);
            }
        }

        else {
            var output = getoutput();
            var history = gethistory();

            if(output=="" && history!="") {
                if(isNaN(history[history.length-1])) {
                    history = history.substring(0, history.length-1)
                }
            }

            if(output != "" || history!="") {
                if(output=="") {
                    output = output;
                }
                else {
                    output = reversenumberformat(output);
                }

                history = history + output;

                if(this.id == "=") {
                    var result = eval(history);
                    displayoutput(result);
                    displayhistory("");
                }
                else {
                    history = history + this.id;
                    displayhistory(history);
                    displayoutput("");
                }
            }
        }
    });
}

var number = document.getElementsByClassName("number");

for(var i=0; i<number.length; i++) {
    number[i].addEventListener("click", function() {
        var output = reversenumberformat(getoutput());

        if(output != NaN) {
            output = output + this.id;
            displayoutput(output);
        }
    });
}