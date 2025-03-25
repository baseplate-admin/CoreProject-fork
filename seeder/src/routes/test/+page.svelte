<script lang="ts">
    let atom_count = $state(0);
</script>

<div class="relative flex h-40 w-40 items-center justify-center rounded-full">
    <!-- Sun -->

    <!-- Orbit 1 -->
    <div
        class="animate-orbit-1 absolute h-[10vh] w-[10vh] rounded-full border-2 border-dashed border-white opacity-100"
    >
        <one-s-one
            class="planet animate-planet-1 absolute left-1/4 top-0 h-4 w-4 rounded-full bg-white"
        ></one-s-one>
        <one-s-two
            class="planet animate-planet-1 absolute bottom-0 right-1/4 h-4 w-4 rounded-full bg-white"
        ></one-s-two>
    </div>

    <!-- Orbit 2 -->
    <div
        class="animate-orbit-2 absolute h-[14vh] w-[14vh] rounded-full border-2 border-dashed border-white opacity-90"
    >
        <div
            class="planet animate-planet-1 absolute left-1/4 top-0 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute left-2/4 top-0 h-4 w-4 -translate-y-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute bottom-0 right-1/4 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute bottom-0 right-2/4 h-4 w-4 translate-y-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute left-0 top-1/4 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute left-0 top-2/4 h-4 w-4 -translate-x-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute bottom-1/4 right-0 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute bottom-2/4 right-0 h-4 w-4 translate-x-2 rounded-full bg-white"
        ></div>
    </div>

    <!-- Orbit 3 -->
    <div
        class="animate-orbit-3 absolute h-[18vh] w-[18vh] rounded-full border-2 border-dashed border-white opacity-90"
    >
        <div
            class="planet animate-planet-1 absolute left-1/4 top-0 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute left-2/4 top-0 h-4 w-4 -translate-y-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute bottom-0 right-1/4 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute bottom-0 right-2/4 h-4 w-4 translate-y-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute left-0 top-1/4 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute left-0 top-2/4 h-4 w-4 -translate-x-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute bottom-1/4 right-0 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute bottom-2/4 right-0 h-4 w-4 translate-x-2 rounded-full bg-white"
        ></div>
    </div>

    <!-- Orbit 4 -->
    <div
        class="animate-orbit-4 absolute h-[22vh] w-[22vh] rounded-full border-2 border-dashed border-white opacity-90"
    >
        <div
            class="planet animate-planet-1 absolute left-1/4 top-0 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute left-2/4 top-0 h-4 w-4 -translate-y-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute bottom-0 right-1/4 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute bottom-0 right-2/4 h-4 w-4 translate-y-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute left-0 top-1/4 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute left-0 top-2/4 h-4 w-4 -translate-x-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute bottom-1/4 right-0 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute bottom-2/4 right-0 h-4 w-4 translate-x-2 rounded-full bg-white"
        ></div>
    </div>

    <!-- Orbit 5 -->
    <div
        class="animate-orbit-5 absolute h-[26vh] w-[26vh] rounded-full border-2 border-dashed border-white opacity-90"
    >
        <div
            class="planet animate-planet-1 absolute left-1/4 top-0 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute left-2/4 top-0 h-4 w-4 -translate-y-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute bottom-0 right-1/4 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute bottom-0 right-2/4 h-4 w-4 translate-y-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute left-0 top-1/4 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute left-0 top-2/4 h-4 w-4 -translate-x-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute bottom-1/4 right-0 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute bottom-2/4 right-0 h-4 w-4 translate-x-2 rounded-full bg-white"
        ></div>
    </div>

    <!-- Orbit 6 -->
    <div
        class="animate-orbit-6 absolute h-[30vh] w-[30vh] rounded-full border-2 border-dashed border-white opacity-50"
    >
        <div
            class="planet animate-planet-1 absolute left-1/4 top-0 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute left-2/4 top-0 h-4 w-4 -translate-y-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute bottom-0 right-1/4 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute bottom-0 right-2/4 h-4 w-4 translate-y-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute left-0 top-1/4 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute left-0 top-2/4 h-4 w-4 -translate-x-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute bottom-1/4 right-0 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute bottom-2/4 right-0 h-4 w-4 translate-x-2 rounded-full bg-white"
        ></div>
    </div>

    <!-- Orbit 7 -->
    <div
        class="animate-orbit-7 absolute h-[34vh] w-[34vh] rounded-full border-2 border-dashed border-white opacity-40"
    >
        <div
            class="planet animate-planet-1 absolute left-1/4 top-0 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute left-2/4 top-0 h-4 w-4 -translate-y-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute bottom-0 right-1/4 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute bottom-0 right-2/4 h-4 w-4 translate-y-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute left-0 top-1/4 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute left-0 top-2/4 h-4 w-4 -translate-x-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute bottom-1/4 right-0 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute bottom-2/4 right-0 h-4 w-4 translate-x-2 rounded-full bg-white"
        ></div>
    </div>

    <!-- Orbit 8 -->
    <div
        class=" animate-orbit-8 absolute h-[38vh] w-[38vh] rounded-full border-2 border-dashed border-white opacity-30"
    >
        <div
            class="planet animate-planet-1 absolute left-1/4 top-0 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute left-2/4 top-0 h-4 w-4 -translate-y-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute bottom-0 right-1/4 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute bottom-0 right-2/4 h-4 w-4 translate-y-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute left-0 top-1/4 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute left-0 top-2/4 h-4 w-4 -translate-x-2 rounded-full bg-white"
        ></div>

        <div
            class="planet animate-planet-1 absolute bottom-1/4 right-0 h-4 w-4 rounded-full bg-white"
        ></div>
        <div
            class="planet animate-planet-1 absolute bottom-2/4 right-0 h-4 w-4 translate-x-2 rounded-full bg-white"
        ></div>
    </div>
</div>

<style>
    @keyframes orbit1 {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }

    @keyframes orbit2 {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(-360deg);
        }
    }

    /* Different speeds for different orbits */
    .animate-orbit-1 {
        animation: orbit1 10s linear infinite;
    }

    .animate-orbit-2 {
        animation: orbit2 15s linear infinite;
    }

    .animate-orbit-3 {
        animation: orbit1 20s linear infinite;
    }

    .animate-orbit-4 {
        animation: orbit2 25s linear infinite;
    }

    .animate-orbit-5 {
        animation: orbit1 30s linear infinite;
    }

    .animate-orbit-6 {
        animation: orbit2 35s linear infinite;
    }

    .animate-orbit-7 {
        animation: orbit1 40s linear infinite;
    }

    .animate-orbit-8 {
        animation: orbit2 45s linear infinite;
    }
</style>
