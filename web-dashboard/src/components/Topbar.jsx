export default function Topbar() {
    return (
        <div
            style={{
                width: "100%",
                height: "80px",
                borderBottom: "1px solid rgba(255,255,255,0.05)",
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                padding: "0 30px",
                background: "rgba(8,17,31,0.7)",
                backdropFilter: "blur(12px)",
            }}
        >
            <div>
                <h2
                    style={{
                        fontSize: "1.3rem",
                        color: "#e2e8f0",
                    }}
                >
                    Live Room — Bedroom
                </h2>

                <p
                    style={{
                        color: "#64748b",
                        marginTop: "4px",
                        fontSize: "0.9rem",
                    }}
                >
                    SimuLith Smart Room Simulation
                </p>
            </div>

            <div
                style={{
                    display: "flex",
                    alignItems: "center",
                    gap: "20px",
                    color: "#cbd5e1",
                }}
            >
                <span>21 May 2026</span>
                <span>14:35</span>
                <span style={{ color: "#60a5fa" }}>Rain</span>
            </div>
        </div>
    )
}