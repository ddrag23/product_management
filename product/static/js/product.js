const fields = ['nama_product', 'nomor', 'id_product', 'kategori_id', 'status_id', 'harga']

async function loadProduct(params = '', page = 1) {
    if (params) {
        document.getElementById('reset').style.display = 'block'
    } else {
        document.getElementById('reset').style.display = 'none'

    }
    const json = await fetch(`/api/products/?page=${page}${params}`)
    const data = await json.json()
    const tbBody = document.getElementById("tb-product")
    tbBody.innerHTML = '';  // Clear previous data
    tbBody.innerHTML = render(data.results)
    renderPagination(data.count, params)
    document.getElementById(`number-${page}`).classList.add("active")

}

function renderPagination(total, params) {
    const totalPages = Math.ceil(total / 5);
    const paginationDiv = document.getElementById('pagination');

    paginationDiv.innerHTML = '';  // Clear previous pagination

    for (let i = 1; i <= totalPages; i++) {
        const li = document.createElement('li')
        li.classList.add("page-item")
        li.setAttribute("id", `number-${i}`)
        li.setAttribute("aria-current", "page")
        const pageLink = document.createElement('button');
        pageLink.classList.add("page-link")
        pageLink.textContent = i;
        pageLink.addEventListener('click', () => {
            loadProduct(params, i);
        });
        li.appendChild(pageLink)
        paginationDiv.appendChild(li);
    }
}


function addValidation(el, value) {
    const pesan = document.getElementById(el)
    const text = document.querySelector(`.${el}`)
    pesan.classList.add('is-invalid')
    text.classList.add('invalid-feedback')
    text.textContent = value
}

function resetValidation(key) {
    let pesan = document.getElementById(key)
    let text = document.querySelector('.' + key)
    text.classList.remove('invalid-feedback')
    pesan.classList.remove('is-invalid')
    text.innerHTML = ''
}

function onAlert(icon, message) {
    Swal.fire({
        title: 'Pesan!',
        icon: icon,
        text: message,
        showConfirmButton: false,
        timer: 1500,
    })
}

async function showModal(e) {
    const modalToggle = document.getElementById('exampleModal') // relatedTarget
    const modal = bootstrap.Modal.getOrCreateInstance(modalToggle)
    clearForm()
    localStorage.setItem('is_edit', 0)
    modal.show()
}

async function edit(e) {
    if (e.target.classList.contains('edit')) {
        const id = e.target.dataset.id
        const modalToggle = document.getElementById('exampleModal') // relatedTarget
        const modal = bootstrap.Modal.getOrCreateInstance(modalToggle)
        localStorage.setItem("is_edit", 1)
        const response = await fetch(`/api/products/${id}`)
        const data = await response.json()
        fields.forEach(item => {
            document.getElementById(item).value = data[item]
        })
        document.getElementById("id_product").readOnly = true
        modal.show()
    }
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function deleteProduct(e) {
    if (e.target.classList.contains('delete')) {
        const id = e.target.dataset.id
        Swal.fire({
            title: 'Apakah anda yakin untuk menghapus data ini?',
            text: "Data yang sudah terhapus tidak bisa dikembalikan!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, Hapus data!'
        }).then(async (result) => {
            if (result.isConfirmed) {
                const csrfToken = getCookie('csrftoken');
                const response = await fetch(`/api/products/${id}/`, {
                    method: "DELETE", headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrfToken,
                        // 'Content-Type': 'application/x-www-form-urlencoded',
                    },
                })
                if (response.status == 204) {
                    onAlert("success", "Data produk berhasil dihapus")
                    loadProduct()
                }
            }
        })
    }
}

function clearForm() {
    fields.forEach(item => {
        resetValidation(item)
        document.getElementById(item).value = ""
    })
}

function render(products) {
    let html = '';
    products.forEach(data => {
        const segment = `
    <tr>
        <td>${data.nomor}</td>
        <td>${data.nama_product}</td>
        <td>${data.harga}</td>
        <td>${data.kategori}</td>
        <td>${data.status}</td>
        <td>
            <div class="d-flex gap-2">
            <button class="btn btn-primary btn-sm edit" data-id="${data.id_product}">Edit</button>
            <button class="btn btn-danger btn-sm delete" data-id="${data.id_product}">Hapus</button>
            </div>
        </td>
    </tr>
    `
        html += segment
    });
    return html
}
['bisa-dijual', 'tidak-bisa-dijual', 'reset'].forEach((el) => {
    document.getElementById(el).addEventListener('click', async function (e) {
        await loadProduct(el == 'reset' ? '' : `&status=${e.target.dataset.status}`)
    })
})

async function submit(e) {
    e.preventDefault();
    const modalToggle = document.getElementById('exampleModal') // relatedTarget
    const modal = bootstrap.Modal.getOrCreateInstance(modalToggle)
    const formData = {}
    fields.forEach(item => {
        formData[item] = document.getElementById(item).value
    })
    const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    try {
        let response;
        if (localStorage.getItem('is_edit') == 1) {
            response = await fetch(`/api/products/${document.getElementById("id_product").value}/`, {
                method: 'PUT',
                body: JSON.stringify(formData),
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                    // 'Content-Type': 'application/x-www-form-urlencoded',
                },
            })
        } else {
            response = await fetch("/api/products/", {
                method: 'POST',
                body: JSON.stringify(formData),
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                    // 'Content-Type': 'application/x-www-form-urlencoded',
                },
            })
        }

        const data = await response.json()
        if (response.status == 400) {
            onAlert("warning", "Lengkapi formulir")
            Object.entries(data).forEach(([key, value]) => addValidation(key, value[0]))
            throw new Error(JSON.stringify(data))
        }
        if ([201, 200].includes(response.status)) {
            onAlert("success", "Data produk berhasil disimpan")
            modal.hide()
            clearForm()
        }
    } catch (error) {
        console.error(error)
    }
}
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('save-product').addEventListener("click", submit)
    document.getElementById('add-product').addEventListener("click", showModal)
    document.addEventListener("click", edit)
    document.addEventListener("click", deleteProduct)
    loadProduct()
});