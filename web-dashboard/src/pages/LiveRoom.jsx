import { useEffect, useState } from "react"
import roomBase from "../assets/room-base.png"

import {
    LineChart,
    Line,
    ResponsiveContainer
} from "recharts"

export default function LiveRoom() {

    const [temperature, setTemperature] = useState(24.6)
    const [humidity, setHumidity] = useState(58)
    const [power, setPower] = useState(436)

    const [history, setHistory] = useState([
        { temp: 24.6 },
        { temp: 24.7 },
        { temp: 24.5 },
        { temp: 24.8 },
        { temp: 24.6 },
    ])

    useEffect(() => {

        const interval = setInterval(() => {

            setTemperature(prev =>
                +(prev + (Math.random() * 0.6 - 0.3)).toFixed(1)
            )

            setHumidity(prev =>
                Math.max(40,
                    Math.min(80,
                        +(prev + (Math.random() * 2 - 1)).toFixed(0)
                    )
                )
            )

            setPower(prev =>
                Math.max(200,
                    Math.min(700,
                        Math.floor(prev + (Math.random() * 60 - 30))
                    )
                )
            )

            setHistory(prev => {

                const updated = [
                    ...prev,
                    { temp: temperature }
                ]

                if (updated.length > 20) {
                    updated.shift()
                }

                return updated

            })

        }, 2000)

        return () => clearInterval(interval)

    }, [])

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

                    <button className="hover:bg-white/5 rounded-xl px-4 py-3 text-left text-white/70 transition">
                        Monitoring
                    </button>

                    <button className="hover:bg-white/5 rounded-xl px-4 py-3 text-left text-white/70 transition">
                        Devices
                    </button>

                    <button className="hover:bg-white/5 rounded-xl px-4 py-3 text-left text-white/70 transition">
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

                    <div className="flex items-center gap-6">

                        <div className="text-right">
                            <p className="text-white/40 text-xs">
                                Simulation Time
                            </p>

                            <h3 className="text-sm font-medium">
                                21 May 2026 — 14:35
                            </h3>
                        </div>

                        <div className="w-px h-8 bg-white/10" />

                        <div className="flex items-center gap-3">

                            <div className="w-3 h-3 rounded-full bg-green-400 animate-pulse" />

                            <span className="text-sm text-green-300">
                                Live
                            </span>

                        </div>

                    </div>

                </div>

                {/* DASHBOARD AREA */}
                <div className="flex-1 p-8 grid grid-cols-[280px_1fr_280px] gap-6">

                    {/* LEFT PANEL */}
                    <div className="flex flex-col gap-6">

                        <div className="bg-white/5 border border-white/10 rounded-3xl p-5 backdrop-blur-xl">
                            <h3 className="text-white/60 text-sm mb-4">
                                Realtime Telemetry
                            </h3>

                            <div className="space-y-5">

                                <div>
                                    <p className="text-white/50 text-sm">
                                        Temperature
                                    </p>

                                    <h2 className="text-4xl font-semibold mt-1 transition-all duration-500">
                                        {temperature}°C
                                    </h2>

                                    <div className="h-[50px] mt-3">

                                        <ResponsiveContainer width="100%" height="100%">

                                            <LineChart data={history}>

                                                <Line
                                                    type="monotone"
                                                    dataKey="temp"
                                                    stroke="#22d3ee"
                                                    strokeWidth={2}
                                                    dot={false}
                                                    isAnimationActive={true}
                                                />

                                            </LineChart>

                                        </ResponsiveContainer>

                                    </div>
                                </div>

                                <div>
                                    <p className="text-white/50 text-sm">
                                        Humidity
                                    </p>

                                    <h2 className="text-4xl font-semibold mt-1 transition-all duration-500">
                                        {humidity}%
                                    </h2>
                                </div>

                                <div>
                                    <p className="text-white/50 text-sm">
                                        Power Usage
                                    </p>
                                    <p className="text-green-400 text-sm mt-2">
                                        System Active
                                    </p>

                                    <h2 className="text-4xl font-semibold mt-1 transition-all duration-500">
                                        {power}W
                                    </h2>
                                </div>

                            </div>
                        </div>

                    </div>

                    {/* ROOM VIEW */}
                    <div className="bg-[#101c30] border border-cyan-400/10 rounded-[40px] relative overflow-hidden shadow-2xl min-h-[760px]">

                        {/* ROOM IMAGE */}
                        <img
                            src={roomBase}
                            alt="SimuLith Room"
                            className="w-full h-full object-cover opacity-90"
                        />

                        {/* OVERLAY */}
                        <div className="absolute inset-0 bg-gradient-to-br from-cyan-500/10 to-transparent" />

                        <div className="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-cyan-500/5" />

                        <div className="absolute inset-0 backdrop-blur-[1px]" />

                        {/* ROOM GLOW */}
                        <div className="absolute -bottom-20 left-1/2 -translate-x-1/2 w-[500px] h-[200px] bg-cyan-500/10 blur-[120px]" />

                        {/* LIVE AMBIENT GLOW */}
                        <div className="
                                absolute inset-0 pointer-events-none
                                opacity-40
                            ">

                            <div className="absolute top-[20%] left-[15%] w-[250px] h-[250px] bg-cyan-400/10 rounded-full blur-[100px] animate-pulse" />

                            <div className="absolute bottom-[10%] right-[10%] w-[300px] h-[300px] bg-blue-500/10 rounded-full blur-[120px] animate-pulse" />

                        </div>

                        {/* AC AIRFLOW */}
                        <div className="absolute top-[170px] left-[70px]">

                            <div className="relative w-[220px] h-[120px]">

                                <div className="absolute w-[180px] h-[2px] bg-cyan-300/40 blur-sm rounded-full top-2 animate-pulse" />

                                <div className="absolute w-[160px] h-[2px] bg-cyan-300/30 blur-sm rounded-full top-8 animate-pulse" />

                                <div className="absolute w-[190px] h-[2px] bg-cyan-300/20 blur-sm rounded-full top-14 animate-pulse" />

                                <div className="absolute w-[150px] h-[2px] bg-cyan-300/30 blur-sm rounded-full top-20 animate-pulse" />

                            </div>

                        </div>

                        {/* OCCUPANCY VISUALIZATION */}
                        <div className="absolute bottom-[120px] left-[52%] -translate-x-1/2 flex items-center justify-center">

                            {/* OUTER PULSE */}
                            <div className="absolute w-[180px] h-[180px] rounded-full border border-cyan-400/10 animate-ping" />

                            {/* MIDDLE RING */}
                            <div className="absolute w-[120px] h-[120px] rounded-full border border-cyan-300/20" />

                            {/* INNER GLOW */}
                            <div className="absolute w-[60px] h-[60px] rounded-full bg-cyan-400/20 blur-2xl" />

                            {/* AVATAR */}
                            <div className="relative z-10 flex flex-col items-center">

                                <div className="w-[18px] h-[18px] rounded-full bg-cyan-300/80 shadow-[0_0_20px_rgba(34,211,238,0.8)]" />

                                <div className="w-[28px] h-[45px] rounded-full border border-cyan-300/40 bg-cyan-300/10 backdrop-blur-sm mt-1" />

                            </div>

                        </div>

                        {/* WEATHER STATUS */}
                        <div className="absolute top-6 right-6 bg-black/40 border border-white/10 backdrop-blur-md rounded-2xl px-4 py-3">

                            <p className="text-white/50 text-xs">
                                Outdoor Weather
                            </p>

                            <h3 className="text-xl font-semibold mt-1">
                                Rain
                            </h3>

                            <p className="text-cyan-300 text-sm mt-1">
                                23°C • Humid
                            </p>

                        </div>

                        {/* DEVICE STATUS AC CARD */}
                        <div className="absolute top-[160px] left-[40px] bg-black/40 border border-cyan-400/20 backdrop-blur-xl rounded-2xl px-4 py-3">

                            <p className="text-white/50 text-xs">
                                Air Conditioner
                            </p>

                            <div className="flex items-center justify-between gap-6 mt-2">

                                <div>
                                    <h3 className="text-cyan-300 text-xl font-semibold">
                                        24°C
                                    </h3>

                                    <p className="text-green-400 text-sm mt-1">
                                        ON
                                    </p>
                                </div>

                                <div className="w-3 h-3 rounded-full bg-cyan-400 animate-pulse" />

                            </div>

                        </div>


                        {/* ROOM TITLE */}
                        <div className="absolute top-6 left-6 bg-black/40 border border-white/10 backdrop-blur-md rounded-2xl px-5 py-3">

                            <p className="text-white/50 text-sm">
                                Smart Room
                            </p>

                            <h2 className="text-2xl font-semibold mt-1">
                                SimuLith Gen-1
                            </h2>

                        </div>

                        {/* LIVE SENSOR CARD */}
                        <div className="absolute bottom-6 right-6 bg-black/50 border border-cyan-400/20 backdrop-blur-xl rounded-2xl px-5 py-4">

                            <div className="flex items-center gap-6">

                                <div>
                                    <p className="text-white/50 text-xs">
                                        Temperature
                                    </p>

                                    <h3 className="text-2xl font-semibold text-cyan-300">
                                        24.6°C
                                    </h3>
                                </div>

                                <div>
                                    <p className="text-white/50 text-xs">
                                        Humidity
                                    </p>

                                    <h3 className="text-2xl font-semibold text-cyan-300">
                                        58%
                                    </h3>
                                </div>

                            </div>

                        </div>

                    </div>

                    {/* RIGHT PANEL */}
                    <div className="flex flex-col gap-6">

                        <div className="bg-white/5 border border-white/10 rounded-3xl p-5 backdrop-blur-xl">
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