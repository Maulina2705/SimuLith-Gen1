const mockWorldState = {

    weather: {
        type: "Light Rain",
        outsideTemp: 23
    },

    human: {
        activity: "Gaming",
        occupancy: true
    },

    environment: {
        temperature: 24.6,
        humidity: 58,
        brightness: 42
    },

    devices: {

        ac: {
            state: "ON",
            power: 320
        },

        pc: {
            state: "ACTIVE",
            power: 180
        },

        lamp: {
            state: "ON"
        }

    },

    energy: {
        totalPower: 436
    }

}

export default mockWorldState