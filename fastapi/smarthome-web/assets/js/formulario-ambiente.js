const base_url = 'https://smarthome-api-c5fj.onrender.com/ambientes'

async function main(){
  const form = document.getElementById('formulario-ambiente')

  form.addEventListener('submit', processar)

}

async function processar(event){

  event.preventDefault()

  const cx_descricao = document.getElementById('descricao')

  const descricao = cx_descricao.value

  // alert(`Você digitou: ${descricao}`)

  const init = {
    method: 'POST',
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({descricao: descricao})
  }

  const response = await fetch(base_url, init)

  if (response.ok){
    alert('Ambiente Salvo com sucesso!')
    window.location = '/'
  }else{
    alert('Error ao processar!')
  }
}

main()