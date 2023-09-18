'use client'

import { Card, CardBody } from "@nextui-org/react"

export default function Rooms(){

  const rooms = [
    {descricao: 'Sala'},
    {descricao: 'Banheiro'},
    {descricao: 'Banheiro'},
    {descricao: 'Banheiro'},
    {descricao: 'Banheiro'},
    {descricao: 'Banheiro'},
    {descricao: 'Banheiro'},
    {descricao: 'Banheiro'},
    {descricao: 'Banheiro'},
    {descricao: 'Banheiro'},
    {descricao: 'Banheiro'},
]

  return (
    <section className="flex flex-col gap-3 pt-4">
      {rooms && rooms.map(room => (
        <Card key={room.descricao} isPressable={true} onPress={(e) => {alert('ok')}}>
          <CardBody>
            <p>{room.descricao}</p>
          </CardBody>
        </Card>
      ))}
    </section>)
}