import React from "react"
import Main from "../components/Main"

type Props = {
  children: React.ReactNode
}

const DevicesLayout = ({children}: Props) => (
  <Main>
    <h1>Ambientes Cadastrados</h1>
    {/* inject page ou nested layout */}
    {children} 
  </Main>
)

export default DevicesLayout