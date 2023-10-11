import { useRef, useState } from 'react'
import './App.css'
import { ResultadoIMC } from './components/ResultadoIMC'
import { Rodape } from './components/Rodape'
import { Saudacao } from './components/Saudacao'

function App() {

  const [imc, setImc] = useState<number | null>(null)

  const inputPesoRef = useRef(null)
  const inputAlturaRef = useRef(null)

  function handleCalcularIMC(event) {
    event.preventDefault()
    const peso = Number(inputPesoRef.current!.value)
    const altura = Number(inputAlturaRef.current!.value)

    const resultado = peso / (altura ** 2)

    setImc(resultado)

    // const resultado = `
    //     Peso: ${peso}
    //     Altura: ${altura}
    //     IMC = ${IMC.toFixed(2)}
    // `
    // alert(resultado)
  }


  return (
    <>
      <header>My First React App</header>
      <main>
        <h1>Hello React by Rogério Silva</h1>
        <Saudacao destinatario='Caio' tipo='Boa noite' />

        <form onSubmit={handleCalcularIMC}>
          <h2>Calculadora de IMC</h2>
          <input ref={inputPesoRef} type="number" placeholder='Digite seu peso(kg)' step='0.01' />
          <input ref={inputAlturaRef} type='number' placeholder='Agora sua altura(m)' step="0.01" />
          <button type='submit'>Calcular IMC</button>
        </form>

        <div>
          <ResultadoIMC valor={imc} />
        </div>
      </main>
      <Rodape />
    </>
  )
}

export default App
