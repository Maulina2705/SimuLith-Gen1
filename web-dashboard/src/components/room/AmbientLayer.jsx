export default function AmbientLayer({ world }) {

    return (

        <>

            {/* OVERLAY */}
            <div className="absolute inset-0 bg-gradient-to-br from-cyan-500/10 to-transparent" />

            <div className="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-cyan-500/5" />

            <div className="absolute inset-0 backdrop-blur-[1px]" />

            {/* CINEMATIC VIGNETTE */}
            <div className="
                absolute inset-0
                bg-[radial-gradient(circle_at_center,transparent_40%,rgba(0,0,0,0.65)_100%)]
                pointer-events-none
            " />

            {/* ATMOSPHERIC LIGHT */}
            <div className="
                absolute top-[18%] left-[25%]
                w-[500px]
                h-[300px]
                bg-cyan-400/5
                blur-[120px]
                rotate-[-8deg]
                pointer-events-none
            " />

            {/* ROOM GLOW */}
            <div className="
                absolute -bottom-20 left-1/2 
                -translate-x-1/2 
                w-[500px] 
                h-[200px] 
                bg-cyan-500/10 
                blur-[120px]
            " />

            {/* LIVE AMBIENT GLOW */}
            <div
                className="
                    absolute inset-0 
                    pointer-events-none
                    transition-all duration-1000
                "
            >

                {/* COOL AMBIENCE */}
                <div
                    className={`
                        absolute top-[20%] left-[15%]
                        w-[250px] h-[250px]
                        rounded-full blur-[100px]
                        transition-all duration-1000

                        ${world.weather.type.includes("Rain")
                            ? "bg-cyan-400/20"
                            : "bg-orange-300/10"
                        }
                    `}
                />

                {/* POWER AMBIENCE */}
                <div
                    className={`
                        absolute bottom-[10%] right-[10%]
                        w-[300px] h-[300px]
                        rounded-full blur-[120px]
                        transition-all duration-1000

                        ${world.energy.totalPower > 500
                            ? "bg-purple-500/20"
                            : "bg-blue-500/10"
                        }
                    `}
                />

            </div>

        </>

    )
}