export default function DeviceEffects({ world }) {

    return (

        <>

            {/* AC AIRFLOW */}
            {world.devices.ac.state === "ON" && (

                <div className="absolute top-[170px] left-[70px]">

                    <div className="relative w-[220px] h-[120px]">

                        <div className="absolute w-[180px] h-[2px] bg-cyan-300/40 blur-sm rounded-full top-2 animate-pulse" />

                        <div className="absolute w-[160px] h-[2px] bg-cyan-300/30 blur-sm rounded-full top-8 animate-pulse" />

                        <div className="absolute w-[190px] h-[2px] bg-cyan-300/20 blur-sm rounded-full top-14 animate-pulse" />

                        <div className="absolute w-[150px] h-[2px] bg-cyan-300/30 blur-sm rounded-full top-20 animate-pulse" />

                    </div>

                </div>

            )}

        </>

    )
}