
let temp = ''

function getvalue(i){
    temp = i
    localStorage.setItem('kota', temp)
}

let search = false;
console.log(temp)

function addheader3(){
    const head = document.getElementById('header3')
    const judulhead = localStorage.getItem('kota')

    head.innerHTML = ""
    const html = `
    <h1><b>Samsat Keliling</b></h1>
    <h3>${judulhead}</h3>
    `;
    head.innerHTML += html;
}

function adddata(){
    const kota = localStorage.getItem('kota')

    const table = document.getElementById('data-table');

    fetch(`/api/Samling?kota_kabupaten=${kota}`)
    .then(response => response.json())
    .then(data => {

        console.log(kota);

        table.innerHTML = ""
            for(let i = 0; i < data.length; i++){
                const html = `
                    <tr>
                        <td style="vertical-align : middle;">${[i+1]}</td>
                        <td >${data[i].lokasi}</td>
                        <td >${data[i].alamat}</td>
                        <td style="vertical-align : middle;">${data[i].waktu_buka}</td>
                        <td style="vertical-align : middle;">${data[i].waktu_tutup}</td>
                        <td style="vertical-align : middle;">${data[i].hari}</td>
                    </tr>
                `;
                table.innerHTML += html;
            }
    })
}



adddata();
addheader3();
