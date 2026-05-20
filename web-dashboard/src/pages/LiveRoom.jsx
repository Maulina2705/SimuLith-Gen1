import mockWorldState from "../data/mockWorldState"
import { useEffect, useState } from "react"

import {
    LineChart,
    Line,
    ResponsiveContainer
} from "recharts"

import DeviceCard from "../components/ui/DeviceCard"
import SensorNode from "../components/ui/SensorNode"
import RoomBase from "../components/room/RoomBase"
import AmbientLayer from "../components/room/AmbientLayer"

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
                                        {mockWorldState.environment.temperature}°C
                                    </h2>

                                    <div className="h-[50px] mt-3">

                                        <ResponsiveContainer width="100%" height="100%">

                                            <LineChart
                                                data={[
                                                    { temp: 24.2 },
                                                    { temp: 24.4 },
                                                    { temp: 24.5 },
                                                    { temp: 24.6 },
                                                    { temp: 24.6 }
                                                ]}
                                            >

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
                                        {mockWorldState.environment.humidity}%
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
                                        {mockWorldState.energy.totalPower}W
                                    </h2>
                                </div>

                            </div>
                        </div>

                    </div>

                    {/* ROOM VIEW */}
                    <div className="bg-[#101c30] border border-cyan-400/10 rounded-[40px] relative overflow-hidden shadow-2xl min-h-[760px]">

                        {/* ROOM IMAGE */}
                        <RoomBase />

                        {/* OVERLAY */}
                        <AmbientLayer world={mockWorldState} />

                        {/* AC AIRFLOW */}
                        {mockWorldState.devices.ac.state === "ON" && (

                            <div className="absolute top-[170px] left-[70px]">

                                <div className="relative w-[220px] h-[120px]">

                                    <div className="absolute w-[180px] h-[2px] bg-cyan-300/40 blur-sm rounded-full top-2 animate-pulse" />

                                    <div className="absolute w-[160px] h-[2px] bg-cyan-300/30 blur-sm rounded-full top-8 animate-pulse" />

                                    <div className="absolute w-[190px] h-[2px] bg-cyan-300/20 blur-sm rounded-full top-14 animate-pulse" />

                                    <div className="absolute w-[150px] h-[2px] bg-cyan-300/30 blur-sm rounded-full top-20 animate-pulse" />

                                </div>

                            </div>

                        )}

                        {/* OCCUPANCY VISUALIZATION */}
                        {mockWorldState.human.occupancy && (

                            <div className="absolute bottom-[120px] left-[52%] -translate-x-1/2 flex items-center justify-center">

                                <div className="absolute w-[180px] h-[180px] rounded-full border border-cyan-400/10 animate-ping" />

                                <div className="absolute w-[120px] h-[120px] rounded-full border border-cyan-300/20" />

                                <div className="absolute w-[60px] h-[60px] rounded-full bg-cyan-400/20 blur-2xl" />

                                <div className="relative z-10 flex flex-col items-center">

                                    <div className="w-[18px] h-[18px] rounded-full bg-cyan-300/80 shadow-[0_0_20px_rgba(34,211,238,0.8)]" />

                                    <div className="w-[28px] h-[45px] rounded-full border border-cyan-300/40 bg-cyan-300/10 backdrop-blur-sm mt-1" />

                                </div>

                            </div>

                        )}

                        {/* WEATHER STATUS */}
                        <div className="absolute top-6 right-6 bg-black/40 border border-white/10 backdrop-blur-md rounded-2xl px-4 py-3">

                            <p className="text-white/50 text-xs">
                                Outdoor Weather
                            </p>

                            <h3 className="text-xl font-semibold mt-1">
                                {mockWorldState.weather.type}
                            </h3>

                            <p className="text-cyan-300 text-sm mt-1">
                                23°C • Humid
                            </p>

                        </div>

                        <DeviceCard
                            title="Air Conditioner"
                            value="24°C"
                            status="ON"
                            top="140px"
                            left="40px"
                        />

                        <DeviceCard
                            title="Workstation"
                            value="124W"
                            status="ACTIVE"
                            top="170px"
                            left="330px"
                        />

                        <DeviceCard
                            title="Rice Cooker"
                            value="210W"
                            status="COOKING"
                            top="270px"
                            left="1085px"
                            color="orange"
                        />

                        <DeviceCard
                            title="PIR Sensor"
                            value="Occupancy"
                            status="Detected"
                            top="620px"
                            left="490px"
                        />

                        {/* SENSOR NODES */}

                        <SensorNode
                            label="S1 PIR"
                            top="540px"
                            left="520px"
                            active={mockWorldState.human.occupancy}
                        />

                        <SensorNode
                            label="S2 Temp"
                            top="430px"
                            left="480px"
                        />

                        <SensorNode
                            label="S3 Outdoor Lux"
                            top="120px"
                            left="300px"
                        />

                        <SensorNode
                            label="S4 Indoor Lux"
                            top="350px"
                            left="600px"
                        />

                        <SensorNode
                            label="S5 Door"
                            top="290px"
                            left="880px"
                        />

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
                                        {mockWorldState.environment.temperature}°C
                                    </h3>
                                </div>

                                <div>
                                    <p className="text-white/50 text-xs">
                                        Humidity
                                    </p>

                                    <h3 className="text-2xl font-semibold text-cyan-300">
                                        {mockWorldState.environment.humidity}%
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
                                        {mockWorldState.human.activity}
                                    </h2>
                                </div>

                                <div>
                                    <p className="text-white/50 text-sm">
                                        Weather
                                    </p>

                                    <h2 className="text-2xl font-semibold mt-1">
                                        {mockWorldState.weather.type}
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