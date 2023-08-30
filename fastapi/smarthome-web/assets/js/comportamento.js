async function main(){

  const base_url = 'https://smarthome-api-c5fj.onrender.com/ambientes'

  // console.log('Requisitando AMBIENTES...')
  const response = await fetch(base_url)

  const status = response.status

  // alert(`Respondeu com status: ${status}`)

  if (status === 200){
    const ambientes = await response.json()
    // console.log(ambientes)
    for (let ambiente of ambientes){
      adicionar_ambiente(ambiente.id, ambiente.descricao)
    }
  }

  // adicionar_ambiente('444', 'Banheiro Social')
  // adicionar_ambiente('446664', 'Despensa')
}


function adicionar_ambiente(id, descricao){
  const ambientes = document.getElementById('ambientes')

  const item = document.createElement('tr')
  const coluna_id = document.createElement('td')
  const coluna_desc = document.createElement('td')

  coluna_id.textContent = id
  coluna_desc.textContent = descricao

  item.append(coluna_id, coluna_desc)
  ambientes.appendChild(item)
}

main()