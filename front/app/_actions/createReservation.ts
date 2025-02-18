"use server";

import createReservationsClient from "@/protos/reservations";
import { CreateReservationRequest } from "@/protos/types/reservations/CreateReservationRequest";
import { CreateReservationResponse } from "@/protos/types/reservations/CreateReservationResponse";

export default async function createReservation({
    checkIn,
    checkOut,
    guests,
    origin,
    destination,
}: CreateReservationRequest): Promise<CreateReservationResponse> {
    const reservationsClient = createReservationsClient();
    return new Promise((resolve, reject) => {
        reservationsClient.BookHotel(
            {
                checkIn: checkIn.toISOString(),
                checkOut: checkOut.toISOString(),
                guests: guests,
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
