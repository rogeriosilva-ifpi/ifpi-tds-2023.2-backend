interface SaudacaoProps {
  destinatario: string
  tipo?: 'Bom dia' | 'Boa tarde' | 'Boa noite'
}


export function Saudacao({ destinatario, tipo = 'Boa tarde' }: SaudacaoProps) {
  return <h1>Olá {destinatario}, {tipo}!</h1>
}