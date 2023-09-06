const base_url = 'https://smarthome-api-c5fj.onrender.com/ambientes'

async function main(){

  reload_ambientes()

}

async function reload_ambientes(){
  // console.log('Requisitando AMBIENTES...')
  const response = await fetch(base_url)

  const status = response.status

  // alert(`Respondeu com status: ${status}`)

  if (status === 200){
    const ambientes = await response.json()
    
    const table_ambientes = document.getElementById('ambientes')
    table_ambientes.innerHTML = ''

    for (let ambiente of ambientes){
      adicionar_ambiente(ambiente.id, ambiente.descricao)
    }
  }
}

function adicionar_ambiente(id, descricao){
  const table_ambientes = document.getElementById('ambientes')

  const linha_item = document.createElement('tr')
  const coluna_id = document.createElement('td')
  const coluna_desc = document.createElement('td')
  const coluna_acoes = document.createElement('td')
  const link_remover = document.createElement('a')

  coluna_id.textContent = id
  coluna_desc.textContent = descricao
  link_remover.textContent = 'Remover'
  // link_remover.href = 'http://www.uol.com.br'
  link_remover.classList.add('botao-table')

  link_remover.onclick = async () => {

    if (!confirm(`Deseja remover "${descricao}"?`)){
      return
    }

    link_remover.textContent = 'Aguarde!!'

    // alert(`Clicou no ID=${id}`)
    const url_remover = base_url + '/' + id
    const init = {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      }
    }
    const response = await fetch(url_remover, init)

    if (response.ok){
      alert(`Ambiente "${descricao}" removido!`)
      reload_ambientes()
    }else{
      alert('Não foi possível remover!')
    }
  }

  coluna_acoes.appendChild(link_remover)

  linha_item.append(coluna_id, coluna_desc, coluna_acoes)
  table_ambientes.appendChild(linha_item)
}

main()