//Python
const { PythonShell } = require("python-shell");
var path = require("path");
//Funcion que Incializa el arreglo de Automatas
var options = {
    // mode: 'json',
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
        arrValidateCoords = []
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
                arrValidateCoords.push(parseFloat(arrXVal[index]))
                arrValidateCoords.push(parseFloat(arrYVal[index]))
            }
        }
        console.log(arrValidateCoords);
        //
        options.args = arrValidateCoords
        let PythonScript = new PythonShell('readJson.py', options);
        //Llamaos al script
        PythonScript.on('message', function(jsonString) {
            console.log(jsonString)
                //Crear grafica
            var myPlot = document.getElementById('graphContent');
            var xy = new Float32Array(arrValidateCoords);

            data = [{ xy: xy, type: 'pointcloud' }];
            layout = {
                title: "Grafica Generada",
                xaxis: {
                    type: "linear",
                    range: [
                        Math.min(arrXVal) - 2,
                        Math.max(arrXVal) + 2
                    ],
                    autorange: false
                },
                yaxis: {
                    type: "linear",
                    range: [
                        Math.min(arrYVal) - 2,
                        Math.max(arrYVal) + 2
                    ],
                    autorange: false
                },
                // height: 598,
                // width: 1080,
                autosize: true,
                showlegend: false
            };

            Plotly.newPlot('graphContent', data, layout);
        });
    });

});