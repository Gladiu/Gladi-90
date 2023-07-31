var participantData = [];

document.getElementById("edit").addEventListener("click", function()
{
    var fields = document.querySelectorAll("table input[type='number']");
    for (var i = 0; i < fields.length; i++)
    {
        fields[i].readOnly = false;
    }
  
    document.getElementById("save").style.display = "inline-block";
});
  
document.getElementById("save").addEventListener("click", function()
{
  
    var fields = document.querySelectorAll("table input[type='number']");
    for (var i = 0; i < fields.length; i++)
    {
        participantData[i].seed = parseInt(fields[i].value);
        fields[i].readOnly = true;
    }
  
    document.getElementById("save").style.display = "none";

    exportData();
    
});

function parseData(json_data)
{

    // Draw table
    var tbodyRef = document.getElementById('participant_table').getElementsByTagName('tbody')[0];

    for (var i = 0, len = json_data.length; i < len; ++i) {

        var newRow = tbodyRef.insertRow();

        newRow.insertCell(0).textContent = json_data[i].id;
        newRow.insertCell(1).textContent = json_data[i].nick;
        var seedCell = newRow.insertCell(2)
        var seedInput = document.createElement("input")
        seedInput.name = "seed" + i;
        seedInput.type = "number";
        seedInput.value = json_data[i].seed;
        seedInput.readOnly = true
        seedCell.appendChild(seedInput)

        // Copy data to internal structure
        var newParticipant = {
            id: json_data[i].id,
            seed: json_data[i].seed,
        };
 
        participantData[i] = newParticipant;

    }
}

function exportData()
{

    $.ajax({
        type: "POST",
        url: "http://localhost/website_src/save_data.php",
        data: JSON.stringify(participantData),
    }).done(function() {
        alert("Data has been submited to the bot");
    });
}

var imported_tournament_info = null
fetch("http://localhost/shared_data/tournament_info.json")
.then((response) => response.json())
.then((json) => parseData(json));
