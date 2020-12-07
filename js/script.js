//Python
const { PythonShell } = require("python-shell");
var path = require("path");
//Funcion que Incializa el arreglo de Automatas
var options = {
    mode: 'json',
    pythonOptions: ['-u'],
    scriptPath: path.join(__dirname, 'engine/'),
    args: []
};
//Documento JS
$(document).ready(function() {
    //Obtener Valores de las coordenadas
    arrXVal = [5]
    arrYVal = [5]
        //
    $("#calcBtn").click(function(e) {
        e.preventDefault();
        let arrArgumetns = ["I500000", "P10"];
        //Verificar numero de interaciones y poblacion
        let numInter = $("input#inter").val();
        let numPob = $("input#pob").val();
        if (numInter !== '') {
            arrArgumetns[0] = "I" + numInter;
        }
        if (numPob !== '') {
            arrArgumetns[1] = "P" + numPob;
        }
        //Obetner coordenadas
        arrXVal[0] = $(".inputNumber#valx1").val();
        arrYVal[0] = $(".inputNumber#valy1").val();
        arrXVal[1] = $(".inputNumber#valx2").val();
        arrYVal[1] = $(".inputNumber#valy2").val();
        arrXVal[2] = $(".inputNumber#valx3").val();
        arrYVal[2] = $(".inputNumber#valy3").val();
        arrXVal[3] = $(".inputNumber#valx4").val();
        arrYVal[3] = $(".inputNumber#valy4").val();
        arrXVal[4] = $(".inputNumber#valx5").val();
        arrYVal[4] = $(".inputNumber#valy5").val();
        for (let index = 0; index < 5; index++) {
            if (arrXVal[index] !== '' && arrYVal[index] !== '') {
                arrArgumetns.push(parseFloat(arrXVal[index]))
                arrArgumetns.push(parseFloat(arrYVal[index]))
            }
        }
        console.log(arrArgumetns);
        //Mostrar mensaje
        let resultContainer = $("#result-container");
        resultContainer.fadeOut();
        $("#process").fadeIn(500);
        //Preparar script de python
        options.args = arrArgumetns
        let PythonScript = new PythonShell('readJson.py', options);
        //Llamaos al script
        PythonScript.on('message', function(jsonString) {
            console.log(jsonString);
            if (jsonString.S.length == 2) {
                var m = jsonString.S[0];
                var b = jsonString.S[1];
                //Html final
                let html = "f(x)<sub>1</sub> = " + m + " x + " + b;
                resultContainer.find("h3#lineal").html("").html(html);
            } else {
                var m = Math.max.apply(null, arrXVal);
                var k = jsonString.S[0];
                //Html final
                let html = "f(x)<sub>2</sub> = e<sup>-" + k + "(x - " + m + ")<sup>2</sup></sup>"
                resultContainer.find("h3#exp").html("").html(html);
                //Ocultar Mensaje
                $("#process").fadeOut(500);
                //Mostrar resultado
                resultContainer.fadeIn(500);
            }

            //Crear grafica
            // var myPlot = document.getElementById('graphContent');
            // var xy = new Float32Array(arrValidateCoords);

            // data = [{ xy: xy, type: 'pointcloud' }];
            // layout = {
            //     title: "Puntos en la grafica",
            //     xaxis: {
            //         type: "linear",
            //         range: [
            //             Math.min(arrXVal) - 2,
            //             Math.max(arrXVal) + 2
            //         ],
            //         autorange: false
            //     },
            //     yaxis: {
            //         type: "linear",
            //         range: [-0.5, 1.5],
            //         autorange: false
            //     },
            //     // height: 598,
            //     // width: 1080,
            //     autosize: true,
            //     showlegend: false
            // };

            // Plotly.newPlot('graphContent', data, layout);
        });
    });

});