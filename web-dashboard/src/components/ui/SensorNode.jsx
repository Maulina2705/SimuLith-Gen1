export default function SensorNode({
    label,
    top,
    left,
    active = true
}) {

    return (
        <div
            className="absolute z-40 flex flex-col items-center"
            style={{
                top,
                left
            }}
        >

            {/* PULSE */}
            <div className={`
                absolute w-[38px] h-[38px]
                rounded-full
                border
                animate-pulse
                ${active
                    ? "border-cyan-400/30"
                    : "border-white/10"
                }
            `} />

            {/* MAIN NODE */}
            <div className={`
                relative
                w-[16px]
                h-[16px]
                rounded-full
                border
                backdrop-blur-xl
                shadow-[0_0_20px_rgba(34,211,238,0.4)]

                ${active
                    ? "bg-cyan-300 border-cyan-200"
                    : "bg-white/20 border-white/20"
                }
            `} />

            {/* LABEL */}
            <div className="
                mt-3
                px-3 py-1
                rounded-full
                bg-black/40
                border border-white/10
                backdrop-blur-xl
            ">

                <p className="text-[11px] text-cyan-200 whitespace-nowrap">
                    {label}
                </p>

            </div>

        </div>
    )
}