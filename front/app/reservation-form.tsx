"use client";

import { Button } from "@/components/ui/button";
import { DatePickerWithRange } from "@/components/ui/date-picker-with-range";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Airplane, Calendar, MapPin, Users } from "@phosphor-icons/react";
import { useCallback, useEffect, useState } from "react";
import type { DateRange } from "react-day-picker";
import { toast } from "sonner";

interface ReservationData {
    checkIn: Date;
    checkOut?: Date;
    guests: number;
    origin: string;
    destination: string;
}

export function ReservationForm() {
    const [formData, setFormData] = useState<ReservationData>({
        checkIn: new Date(),
        checkOut: undefined,
        guests: 1,
        origin: "",
        destination: "",
    });
    const [dateRange, setDateRange] = useState<DateRange | undefined>(
        undefined
    );

    const handleSubmit = useCallback(
        (e: React.FormEvent) => {
            e.preventDefault();
            toast.info("Reservation Data:", {
                description: JSON.stringify(formData, null, 2),
            });
            // Here you would typically send the data to your backend
        },
        [formData]
    );

    useEffect(() => {
        if (dateRange) {
            setFormData({
                ...formData,
                checkIn: dateRange.from ?? new Date(),
                checkOut: dateRange.to,
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
                        value={formData.guests}
                        onChange={(e) =>
                            setFormData({
                                ...formData,
                                guests: parseInt(e.target.value),
                            })
                        }
                        required
                    />
                </div>

                <input
                    type="hidden"
                    name="checkIn"
                    value={formData.checkIn.getTime()}
                />
                <input
                    type="hidden"
                    name="checkOut"
                    value={formData.checkOut?.getTime()}
                />
            </div>

            <Button type="submit" className="ml-auto">
                Buscar Viagem
            </Button>
        </form>
    );
}
