export default function PresenceLayer({ world }) {

    return (

        <>

            {/* OCCUPANCY VISUALIZATION */}
            {world.human.occupancy && (

                <div className="
                    absolute bottom-[120px] 
                    left-[52%] 
                    -translate-x-1/2 
                    flex items-center justify-center
                ">

                    <div className="
                        absolute w-[180px] h-[180px]
                        rounded-full border
                        border-cyan-400/10
                        animate-ping
                    " />

                    <div className="
                        absolute w-[120px] h-[120px]
                        rounded-full border
                        border-cyan-300/20
                    " />

                    <div className="
                        absolute w-[60px] h-[60px]
                        rounded-full
                        bg-cyan-400/20
                        blur-2xl
                    " />

                    <div className="
                        relative z-10
                        flex flex-col items-center
                    ">

                        <div className="
                            w-[18px] h-[18px]
                            rounded-full
                            bg-cyan-300/80
                            shadow-[0_0_20px_rgba(34,211,238,0.8)]
                        " />

                        <div className="
                            w-[28px] h-[45px]
                            rounded-full
                            border border-cyan-300/40
                            bg-cyan-300/10
                            backdrop-blur-sm
                            mt-1
                        " />

                    </div>

                </div>

            )}

        </>

    )
}