import DashboardLayout from "./layouts/DashboardLayout"
import Sidebar from "./components/Sidebar"
import Topbar from "./components/Topbar"

function App() {
  return (
    <DashboardLayout>
      <Sidebar />

      <div
        style={{
          flex: 1,
          display: "flex",
          flexDirection: "column",
        }}
      >
        <Topbar />

        <div
          style={{
            flex: 1,
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            color: "#94a3b8",
            fontSize: "2rem",
          }}
        >
          Live Room Visualization Area
        </div>
      </div>
    </DashboardLayout>
  )
}

export default App