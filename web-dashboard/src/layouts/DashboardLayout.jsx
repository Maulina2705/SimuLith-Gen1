export default function DashboardLayout({ children }) {
    return (
        <div
            style={{
                width: "100%",
                height: "100vh",
                display: "flex",
                background: "#08111f",
            }}
        >
            {children}
        </div>
    )
}