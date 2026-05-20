import roomBase from "../../assets/room-base.png"

export default function RoomBase() {

    return (

        <img
            src={roomBase}
            alt="SimuLith Room"
            className="
                w-full h-full object-cover opacity-90
                scale-[1.02]
                hover:scale-[1.03]
                transition-all duration-[4000ms]
            "
        />

    )
}