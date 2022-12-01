
function getSamling() {
    axios.get('/api/samling')
        .then(function (response) {
            console.log(response.data)
        })
    
    .catch(error => {
        console.log(error)
    })
}

function inserthtml(samling){
    tbody.innerHTML = '';

    for(let i=0; i < samling.length; i++){
        const html = `
        <tr>${samling[i].Lokasi}</tr>
        <tr>${samling[i].Alamat}</tr>
        <tr align="center" valign="middle">${samling[i].Waktu_Buka}</tr>
        <tr align="center" valign="middle">${samling[i].Waktu_Tutup}</tr>
        <tr align="center" valign="middle">${samling[i].Hari}</tr>
    `;
    tbody.innerHTML += html;
    }
}