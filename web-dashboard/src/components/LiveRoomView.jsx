export default function LiveRoomView() {
    return (
        <div
            style={{
                flex: 1,
                display: "flex",
                padding: "24px",
                gap: "24px",
                overflow: "hidden",
            }}
        >
            {/* ROOM AREA */}
            <div
                style={{
                    flex: 1,
                    borderRadius: "28px",
                    background:
                        "linear-gradient(180deg, rgba(17,24,39,0.95), rgba(8,17,31,0.95))",
                    border: "1px solid rgba(255,255,255,0.06)",
                    position: "relative",
                    overflow: "hidden",

                    boxShadow:
                        "0 0 60px rgba(59,130,246,0.08)",
                }}
            >
                {/* Ambient Glow */}
                <div
                    style={{
                        position: "absolute",
                        width: "500px",
                        height: "500px",
                        background:
                            "radial-gradient(circle, rgba(59,130,246,0.18), transparent 70%)",
                        top: "-120px",
                        right: "-120px",
                        filter: "blur(40px)",
                    }}
                />

                {/* Room Placeholder */}
                <div
                    style={{
                        width: "100%",
                        height: "100%",
                        display: "flex",
                        justifyContent: "center",
                        alignItems: "center",
                        flexDirection: "column",
                        position: "relative",
                        zIndex: 2,
                    }}
                >
                    <h1
                        style={{
                            fontSize: "2.5rem",
                            color: "#e2e8f0",
                            marginBottom: "12px",
                        }}
                    >
                        SimuLith Live Room
                    </h1>

                    <p
                        style={{
                            color: "#64748b",
                            fontSize: "1rem",
                        }}
                    >
                        Realtime Smart Room Visualization
                    </p>
                </div>
            </div>

            {/* RIGHT PANEL */}
            <div
                style={{
                    width: "320px",
                    display: "flex",
                    flexDirection: "column",
                    gap: "20px",
                }}
            >
                {/* Telemetry Card */}
                <div
                    style={{
                        padding: "24px",
                        borderRadius: "24px",
                        background: "rgba(15,23,42,0.9)",
                        border: "1px solid rgba(255,255,255,0.05)",
                    }}
                >
                    <h3
                        style={{
                            marginBottom: "20px",
                            color: "#e2e8f0",
                        }}
                    >
                        Realtime Telemetry
                    </h3>

                    <div
                        style={{
                            display: "flex",
                            flexDirection: "column",
                            gap: "18px",
                        }}
                    >
                        <div>
                            <p style={{ color: "#64748b" }}>Temperature</p>
                            <h2 style={{ color: "#e2e8f0" }}>24.6°C</h2>
                        </div>

                        <div>
                            <p style={{ color: "#64748b" }}>Humidity</p>
                            <h2 style={{ color: "#e2e8f0" }}>58%</h2>
                        </div>

                        <div>
                            <p style={{ color: "#64748b" }}>Power Usage</p>
                            <h2 style={{ color: "#60a5fa" }}>436W</h2>
                        </div>
                    </div>
                </div>

                {/* Simulation Context */}
                <div
                    style={{
                        padding: "24px",
                        borderRadius: "24px",
                        background: "rgba(15,23,42,0.9)",
                        border: "1px solid rgba(255,255,255,0.05)",
                    }}
                >
                    <h3
                        style={{
                            marginBottom: "20px",
                            color: "#e2e8f0",
                        }}
                    >
                        Simulation Context
                    </h3>

                    <div
                        style={{
                            display: "flex",
                            flexDirection: "column",
                            gap: "16px",
                        }}
                    >
                        <div>
                            <p style={{ color: "#64748b" }}>Current Activity</p>
                            <h2 style={{ color: "#e2e8f0" }}>Resting</h2>
                        </div>

                        <div>
                            <p style={{ color: "#64748b" }}>Weather</p>
                            <h2 style={{ color: "#60a5fa" }}>Rain</h2>
                        </div>

                        <div>
                            <p style={{ color: "#64748b" }}>Occupancy</p>
                            <h2 style={{ color: "#22c55e" }}>Detected</h2>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}