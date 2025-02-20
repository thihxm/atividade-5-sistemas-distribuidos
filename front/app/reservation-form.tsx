"use client";

import { Button } from "@/components/ui/button";
import { DatePickerWithRange } from "@/components/ui/date-picker-with-range";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
    Airplane,
    ArrowClockwise,
    Calendar,
    MapPin,
    Users,
} from "@phosphor-icons/react";
import { useCallback, useEffect, useState, useTransition } from "react";
import type { DateRange } from "react-day-picker";
import { toast } from "sonner";
import createReservation from "./_actions/createReservation";

interface ReservationData {
    checkInDate: Date;
    checkOutDate?: Date;
    numberOfPeople: number;
    origin: string;
    destination: string;
}

export function ReservationForm() {
    const [formData, setFormData] = useState<ReservationData>({
        checkInDate: new Date(),
        checkOutDate: undefined,
        numberOfPeople: 1,
        origin: "",
        destination: "",
    });
    const [dateRange, setDateRange] = useState<DateRange | undefined>(
        undefined
    );

    const [isReservationPending, startReservation] = useTransition();

    const handleSubmit = useCallback(
        (e: React.FormEvent) => {
            e.preventDefault();
            startReservation(async () => {
                const reservation = await createReservation({
                    checkInDate: {
                        seconds: formData.checkInDate.getTime() / 1000,
                        nanos: 0,
                    },
                    checkOutDate: formData.checkOutDate
                        ? {
                              seconds: formData.checkOutDate.getTime() / 1000,
                              nanos: 0,
                          }
                        : undefined,
                    numberOfPeople: formData.numberOfPeople,
                    origin: formData.origin,
                    destination: formData.destination,
                });
                console.log(reservation);
                if (reservation.success) {
                    toast.success("Reserva criada com sucesso", {
                        description: reservation.message,
                    });
                } else {
                    toast.error("Não foi possível criar a reserva", {
                        description: reservation.message,
                    });
                }
            });
        },
        [formData]
    );

    useEffect(() => {
        if (dateRange) {
            setFormData({
                ...formData,
                checkInDate: dateRange.from ?? new Date(),
                checkOutDate: dateRange.to,
            });
        }
    }, [dateRange]);

    return (
        <form onSubmit={handleSubmit} className="p-6 md:p-8 space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
                <div className="space-y-2 col-span-2">
                    <Label className="flex items-center">
                        <MapPin className="w-4 h-4 mr-2" />
                        Origem
                    </Label>
                    <Input
                        type="text"
                        value={formData.origin}
                        onChange={(e) =>
                            setFormData({
                                ...formData,
                                origin: e.target.value,
                            })
                        }
                        placeholder="De onde você está vindo?"
                        required
                    />
                </div>

                <div className="space-y-2 col-span-2">
                    <Label className="flex items-center">
                        <Airplane className="w-4 h-4 mr-2" />
                        Destino
                    </Label>
                    <Input
                        type="text"
                        value={formData.destination}
                        onChange={(e) =>
                            setFormData({
                                ...formData,
                                destination: e.target.value,
                            })
                        }
                        placeholder="Para onde você quer ir?"
                        required
                    />
                </div>

                <div className="space-y-2 col-auto md:col-span-3">
                    <Label className="flex items-center">
                        <Calendar className="w-4 h-4 mr-2" />
                        Data da Viagem
                    </Label>
                    <DatePickerWithRange
                        value={dateRange}
                        onChange={setDateRange}
                    />
                </div>

                <div className="space-y-2">
                    <Label className="flex items-center">
                        <Users className="w-4 h-4 mr-2" />
                        Número de Hóspedes
                    </Label>
                    <Input
                        type="number"
                        min="1"
                        value={formData.numberOfPeople}
                        onChange={(e) =>
                            setFormData({
                                ...formData,
                                numberOfPeople: parseInt(e.target.value),
                            })
                        }
                        required
                    />
                </div>

                <input
                    type="hidden"
                    name="checkIn"
                    value={formData.checkInDate.getTime()}
                />
                <input
                    type="hidden"
                    name="checkOutDate"
                    value={formData.checkOutDate?.getTime()}
                />
            </div>

            <Button
                type="submit"
                className="ml-auto"
                disabled={isReservationPending}
            >
                {isReservationPending && (
                    <ArrowClockwise className="w-4 h-4 mr-2 animate-spin" />
                )}
                Buscar Viagem
            </Button>
        </form>
    );
}
