const menuItems = [
    "Live Room",
    "Monitoring",
    "Devices",
    "Analytics",
    "Events",
    "Simulation",
]

export default function Sidebar() {
    return (
        <div
            style={{
                width: "240px",
                height: "100%",
                background: "rgba(10, 20, 35, 0.9)",
                borderRight: "1px solid rgba(255,255,255,0.05)",
                padding: "24px",
                display: "flex",
                flexDirection: "column",
                gap: "20px",
            }}
        >
            <h1
                style={{
                    fontSize: "1.8rem",
                    color: "#e2e8f0",
                }}
            >
                SimuLith
            </h1>

            <div
                style={{
                    display: "flex",
                    flexDirection: "column",
                    gap: "12px",
                    marginTop: "30px",
                }}
            >
                {menuItems.map((item) => (
                    <div
                        key={item}
                        style={{
                            padding: "14px 16px",
                            borderRadius: "12px",
                            background:
                                item === "Live Room"
                                    ? "rgba(59,130,246,0.15)"
                                    : "transparent",
                            color:
                                item === "Live Room"
                                    ? "#60a5fa"
                                    : "#94a3b8",
                            cursor: "pointer",
                            transition: "0.3s",
                        }}
                    >
                        {item}
                    </div>
                ))}
            </div>
        </div>
    )
}