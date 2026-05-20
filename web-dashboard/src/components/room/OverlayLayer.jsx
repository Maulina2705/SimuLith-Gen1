import DeviceCard from "../ui/DeviceCard"

export default function OverlayLayer({
    hoveredDevice,
    setHoveredDevice
}) {

    return (

        <>
            <div className=" absolute top-[140px] left-[40px] w-[120px] h-[80px] z-40 " onMouseEnter={() => setHoveredDevice("ac")} onMouseLeave={() => setHoveredDevice(null)} />

            {hoveredDevice === "ac" && (

                <DeviceCard
                    title="Air Conditioner"
                    value="24°C"
                    status="ON"
                    top="140px"
                    left="40px"
                />

            )}

            <div
                className="
                    absolute
                    top-[170px]
                    left-[330px]
                    w-[140px]
                    h-[90px]
                    z-40
                "
                onMouseEnter={() => setHoveredDevice("pc")}
                onMouseLeave={() => setHoveredDevice(null)}
            />

            {hoveredDevice === "pc" && (

                <DeviceCard
                    title="Personal Computer (PC)"
                    value="124W"
                    status="ACTIVE"
                    top="170px"
                    left="330px"
                />

            )}

            <div
                className="
                    absolute
                    top-[270px]
                    left-[1085px]
                    w-[140px]
                    h-[90px]
                    z-40
                "
                onMouseEnter={() => setHoveredDevice("ricecook")}
                onMouseLeave={() => setHoveredDevice(null)}
            />

            {hoveredDevice === "ricecook" && (

                <DeviceCard
                    title="Rice Cooker"
                    value="210W"
                    status="COOKING"
                    top="270px"
                    left="1085px"
                    color="orange"
                />

            )}

            <div
                className="
                    absolute
                    top-[620px]
                    left-[490px]
                    w-[140px]
                    h-[90px]
                    z-40
                "
                onMouseEnter={() => setHoveredDevice("pir")}
                onMouseLeave={() => setHoveredDevice(null)}
            />

            {hoveredDevice === "pir" && (

                <DeviceCard
                    title="PIR Sensor"
                    value="Occupancy"
                    status="Detected"
                    top="620px"
                    left="490px"
                />

            )}
        </>

    )
}