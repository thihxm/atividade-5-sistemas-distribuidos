import { ReservationForm } from "./reservation-form";

export default function Home() {
    return (
        <div className="min-h-screen bg-gradient-to-br from-emerald-50 to-teal-100 p-4 md:p-6 lg:p-8">
            <div className="max-w-4xl mx-auto">
                <div className="bg-white rounded-2xl shadow-xl overflow-hidden">
                    <div
                        className="h-64 bg-cover bg-center"
                        style={{
                            backgroundImage:
                                'url("https://images.unsplash.com/photo-1571896349842-33c89424de2d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80")',
                        }}
                    >
                        <div className="h-full w-full bg-black bg-opacity-50 flex items-center justify-center">
                            <h1 className="text-4xl md:text-5xl font-bold text-white text-center">
                                Encontre a sua próxima viagem
                            </h1>
                        </div>
                    </div>

                    <ReservationForm />
                </div>
            </div>
        </div>
    );
}
