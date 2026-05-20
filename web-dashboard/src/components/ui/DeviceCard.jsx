export default function DeviceCard({
    title,
    value,
    status,
    top,
    left,
    color = "cyan"
}) {

    const glow =
        color === "orange"
            ? "shadow-[0_0_40px_rgba(255,140,0,0.25)]"
            : "shadow-[0_0_40px_rgba(34,211,238,0.2)]"

    const border =
        color === "orange"
            ? "border-orange-400/20"
            : "border-cyan-400/20"

    const text =
        color === "orange"
            ? "text-orange-300"
            : "text-cyan-300"

    return (
        <div
            className={`
                absolute z-30
                bg-black/40
                backdrop-blur-xl
                border
                rounded-2xl
                px-4 py-3
                min-w-[140px]
                transition-all duration-500
                hover:scale-[1.03]
                ${border}
                ${glow}
            `}
            style={{
                top,
                left
            }}
        >

            <p className="text-white/40 text-xs">
                {title}
            </p>

            <div className="flex items-center justify-between mt-2">

                <div>

                    <h3 className={`text-xl font-semibold ${text}`}>
                        {value}
                    </h3>

                    <p className="text-green-400 text-sm mt-1">
                        {status}
                    </p>

                </div>

                <div className={`w-3 h-3 rounded-full animate-pulse ${color === "orange"
                    ? "bg-orange-400"
                    : "bg-cyan-400"
                    }`} />

            </div>

        </div>
    )
}