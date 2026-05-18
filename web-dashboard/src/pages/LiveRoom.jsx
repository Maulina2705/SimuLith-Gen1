export default function LiveRoom() {
    return (
        <div className="w-screen h-screen bg-[#08111f] flex">

            {/* SIDEBAR */}
            <div className="w-[260px] h-full border-r border-white/10 bg-[#0b1728] p-6 flex flex-col">

                <h1 className="text-3xl font-semibold text-cyan-400">
                    SimuLith
                </h1>

                <p className="text-sm text-white/50 mt-1">
                    Smart Room Simulator
                </p>

                <div className="mt-10 flex flex-col gap-3">

                    <button className="bg-cyan-500/20 border border-cyan-400/30 rounded-xl px-4 py-3 text-left text-cyan-300">
                        Live Room
                    </button>

                    <button className="hover:bg-white/5 rounded-xl px-4 py-3 text-left text-white/70">
                        Monitoring
                    </button>

                    <button className="hover:bg-white/5 rounded-xl px-4 py-3 text-left text-white/70">
                        Devices
                    </button>

                    <button className="hover:bg-white/5 rounded-xl px-4 py-3 text-left text-white/70">
                        Analytics
                    </button>

                </div>

            </div>

            {/* MAIN CONTENT */}
            <div className="flex-1 flex flex-col">

                {/* TOPBAR */}
                <div className="h-[80px] border-b border-white/10 flex items-center justify-between px-8">

                    <div>
                        <h2 className="text-2xl font-semibold">
                            Live Room
                        </h2>

                        <p className="text-sm text-white/50">
                            Bedroom Simulation
                        </p>
                    </div>

                    <div className="flex items-center gap-4">

                        <div className="w-3 h-3 rounded-full bg-green-400 animate-pulse" />

                        <span className="text-sm text-green-300">
                            Live
                        </span>

                    </div>

                </div>

                {/* DASHBOARD AREA */}
                <div className="flex-1 p-8 grid grid-cols-[320px_1fr_320px] gap-6">

                    {/* LEFT PANEL */}
                    <div className="flex flex-col gap-6">

                        <div className="bg-white/5 border border-white/10 rounded-3xl p-5">
                            <h3 className="text-white/60 text-sm mb-4">
                                Realtime Telemetry
                            </h3>

                            <div className="space-y-5">

                                <div>
                                    <p className="text-white/50 text-sm">
                                        Temperature
                                    </p>

                                    <h2 className="text-4xl font-semibold mt-1">
                                        24.6°C
                                    </h2>
                                </div>

                                <div>
                                    <p className="text-white/50 text-sm">
                                        Humidity
                                    </p>

                                    <h2 className="text-4xl font-semibold mt-1">
                                        58%
                                    </h2>
                                </div>

                                <div>
                                    <p className="text-white/50 text-sm">
                                        Power Usage
                                    </p>

                                    <h2 className="text-4xl font-semibold mt-1">
                                        436W
                                    </h2>
                                </div>

                            </div>
                        </div>

                    </div>

                    {/* ROOM VIEW */}
                    <div className="bg-[#101c30] border border-white/10 rounded-[40px] relative overflow-hidden">

                        <div className="absolute inset-0 bg-gradient-to-br from-cyan-500/10 to-transparent" />

                        <div className="absolute inset-0 flex items-center justify-center">

                            <h1 className="text-white/20 text-4xl font-bold">
                                ROOM VIEW
                            </h1>

                        </div>

                    </div>

                    {/* RIGHT PANEL */}
                    <div className="flex flex-col gap-6">

                        <div className="bg-white/5 border border-white/10 rounded-3xl p-5">
                            <h3 className="text-white/60 text-sm mb-4">
                                Simulation Context
                            </h3>

                            <div className="space-y-4">

                                <div>
                                    <p className="text-white/50 text-sm">
                                        Current Activity
                                    </p>

                                    <h2 className="text-2xl font-semibold mt-1">
                                        Resting
                                    </h2>
                                </div>

                                <div>
                                    <p className="text-white/50 text-sm">
                                        Weather
                                    </p>

                                    <h2 className="text-2xl font-semibold mt-1">
                                        Rain
                                    </h2>
                                </div>

                            </div>
                        </div>

                    </div>

                </div>

            </div>

        </div>
    )
}