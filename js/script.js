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
                arrValidateCoords.push({ "X": arrXVal[index], "Y": arrYVal[index] })
            }
        }
        console.log(arrValidateCoords)
    })
});