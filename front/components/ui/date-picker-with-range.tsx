"use client";

import { Calendar as CalendarIcon } from "@phosphor-icons/react";
import { format } from "date-fns";
import { ptBR } from "date-fns/locale";
import type { DateRange } from "react-day-picker";

import { Button } from "@/components/ui/button";
import { Calendar } from "@/components/ui/calendar";
import {
    Popover,
    PopoverContent,
    PopoverTrigger,
} from "@/components/ui/popover";
import { cn } from "@/lib/utils";

function formatDate(date: Date) {
    return format(date, "LLL dd, y", { locale: ptBR });
}

interface DatePickerWithRangeProps {
    value?: DateRange | undefined;
    onChange?: (date: DateRange | undefined) => void;
    className?: string;
}

export function DatePickerWithRange({
    value,
    onChange,
    className,
}: DatePickerWithRangeProps) {
    return (
        <div className={cn("grid gap-2", className)}>
            <Popover>
                <PopoverTrigger asChild>
                    <Button
                        id="date"
                        variant={"outline"}
                        className={cn(
                            "min-w-[300px] justify-start text-left font-normal",
                            !value && "text-muted-foreground"
                        )}
                    >
                        <CalendarIcon />
                        {value?.from ? (
                            value.to ? (
                                <>
                                    {formatDate(value.from)} -{" "}
                                    {formatDate(value.to)}
                                </>
                            ) : (
                                formatDate(value.from)
                            )
                        ) : (
                            <span>Selecione a data</span>
                        )}
                    </Button>
                </PopoverTrigger>
                <PopoverContent className="w-auto p-0" align="start">
                    <Calendar
                        initialFocus
                        mode="range"
                        defaultMonth={value?.from}
                        selected={value}
                        onSelect={onChange}
                        numberOfMonths={2}
                    />
                </PopoverContent>
            </Popover>
        </div>
    );
}
