interface ResultadoIMCProps {
  valor: number | null
}

export function ResultadoIMC({ valor }: ResultadoIMCProps) {

  if (valor === null) {
    return <p>IMC não calculado!</p>
  }

  return <p>Seu IMC é {valor.toFixed(2)}</p>
}