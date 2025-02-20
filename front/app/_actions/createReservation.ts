"use server";

import createReservationsClient from "@/protos/travelAgency";
import { Requisicao } from "@/protos/types/gRPC/Requisicao";
import { Resposta } from "@/protos/types/gRPC/Resposta";

export default async function createReservation({
    checkInDate,
    checkOutDate,
    numberOfPeople,
    origin,
    destination,
}: Requisicao): Promise<Resposta> {
    const reservationsClient = createReservationsClient();
    return new Promise((resolve, reject) => {
        reservationsClient.SolicitarPacoteViagem(
            {
                checkInDate: checkInDate,
                checkOutDate: checkOutDate,
                numberOfPeople: numberOfPeople,
                origin: origin,
                destination: destination,
            },
            (err, response) => {
                if (err) reject(err);
                if (response) resolve(response);
            }
        );
    });
}
