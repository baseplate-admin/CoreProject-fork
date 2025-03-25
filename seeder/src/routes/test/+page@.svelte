<script lang="ts">
    import { Server } from 'lucide-svelte';

    let server_count = $state(0);
</script>

<div class="flex flex-col items-center justify-center">
    <div class="text-bold -translate-y-[25vh]">
        <h1 class="bold text-2xl">Looking for other servers on subnet</h1>
    </div>
    <div class="text-bold translate-y-[40vh]">
        <h1 class="bold text-2xl">Found : {server_count}</h1>
    </div>

    <div class="relative flex h-40 w-40 items-center justify-center rounded-full">
        <!-- Sun -->
        <Server class="h-10 w-10" />

        <!-- Orbit 1 -->
        <div
            class="animate-orbit-1 absolute h-[15vh] w-[15vh] rounded-full border-2 border-dashed border-white opacity-100"
        >
            <one
                class="planet animate-planet-1 absolute left-1/4 top-0 h-4 w-4 rounded-full bg-white"
            ></one>
            <two
                class="planet animate-planet-1 absolute bottom-0 right-1/4 h-4 w-4 rounded-full bg-white"
            ></two>
        </div>

        <!-- Orbit 2 -->
        <div
            class="animate-orbit-2 absolute h-[20vh] w-[20vh] rounded-full border-2 border-dashed border-white opacity-90"
        >
            <one
                class="planet animate-planet-1 absolute left-1/4 top-0 h-4 w-4 rounded-full bg-white"
            ></one>
            <two
                class="planet animate-planet-1 absolute left-2/4 top-0 h-4 w-4 -translate-y-2 rounded-full bg-white"
            ></two>

            <three
                class="planet animate-planet-1 absolute bottom-0 right-1/4 h-4 w-4 rounded-full bg-white"
            ></three>
            <four
                class="planet animate-planet-1 absolute bottom-0 right-2/4 h-4 w-4 translate-y-2 rounded-full bg-white"
            ></four>

            <five
                class="planet animate-planet-1 absolute left-0 top-1/4 h-4 w-4 rounded-full bg-white"
            ></five>
            <six
                class="planet animate-planet-1 absolute left-0 top-2/4 h-4 w-4 -translate-x-2 rounded-full bg-white"
            ></six>

            <seven
                class="planet animate-planet-1 absolute bottom-1/4 right-0 h-4 w-4 rounded-full bg-white"
            ></seven>
            <eight
                class="planet animate-planet-1 absolute bottom-2/4 right-0 h-4 w-4 translate-x-2 rounded-full bg-white"
            ></eight>
        </div>

        <!-- Orbit 3 -->
        <div
            class="animate-orbit-3 absolute h-[25vh] w-[25vh] rounded-full border-2 border-dashed border-white opacity-90"
        >
            <one
                class="planet animate-planet-1 absolute left-1/4 top-0 h-4 w-4 rounded-full bg-white"
            ></one>
            <two
                class="planet animate-planet-1 absolute left-2/4 top-0 h-4 w-4 -translate-y-2 rounded-full bg-white"
            ></two>

            <three
                class="planet animate-planet-1 absolute bottom-0 right-1/4 h-4 w-4 rounded-full bg-white"
            ></three>
            <four
                class="planet animate-planet-1 absolute bottom-0 right-2/4 h-4 w-4 translate-y-2 rounded-full bg-white"
            ></four>

            <five
                class="planet animate-planet-1 absolute left-0 top-1/4 h-4 w-4 rounded-full bg-white"
            ></five>
            <six
                class="planet animate-planet-1 absolute left-0 top-2/4 h-4 w-4 -translate-x-2 rounded-full bg-white"
            ></six>

            <seven
                class="planet animate-planet-1 absolute bottom-1/4 right-0 h-4 w-4 rounded-full bg-white"
            ></seven>
            <eight
                class="planet animate-planet-1 absolute bottom-2/4 right-0 h-4 w-4 translate-x-2 rounded-full bg-white"
            ></eight>
        </div>

        <!-- Orbit 4 -->
        <div
            class="animate-orbit-4 absolute h-[30vh] w-[30vh] rounded-full border-2 border-dashed border-white opacity-90"
        >
            <one
                class="planet animate-planet-1 absolute left-1/4 top-0 h-4 w-4 translate-y-1 rounded-full bg-white"
            ></one>
            <two
                class="planet animate-planet-1 absolute left-2/4 top-0 h-4 w-4 -translate-y-3 rounded-full bg-white"
            ></two>

            <three
                class="planet animate-planet-1 absolute bottom-0 right-1/4 h-4 w-4 -translate-y-1 rounded-full bg-white"
            ></three>
            <four
                class="planet animate-planet-1 absolute bottom-0 right-2/4 h-4 w-4 translate-y-3 rounded-full bg-white"
            ></four>

            <five
                class="planet animate-planet-1 absolute left-0 top-1/4 h-4 w-4 translate-y-2 rounded-full bg-white"
            ></five>
            <six
                class="planet animate-planet-1 absolute left-0 top-2/4 h-4 w-4 -translate-x-3 rounded-full bg-white"
            ></six>

            <seven
                class="planet animate-planet-1 absolute bottom-1/4 right-0 h-4 w-4 -translate-y-2 rounded-full bg-white"
            ></seven>
            <eight
                class="planet animate-planet-1 absolute bottom-2/4 right-0 h-4 w-4 translate-x-3 rounded-full bg-white"
            ></eight>
        </div>

        <!-- Orbit 5 -->
        <div
            class="animate-orbit-5 absolute h-[35vh] w-[35vh] rounded-full border-2 border-dashed border-white opacity-90"
        >
            <one
                class="planet animate-planet-1 absolute left-1/4 top-0 h-4 w-4 translate-y-2 rounded-full bg-white"
            ></one>
            <two
                class="planet animate-planet-1 absolute left-2/4 top-0 h-4 w-4 -translate-y-2 rounded-full bg-white"
            ></two>

            <three
                class="planet animate-planet-1 absolute bottom-0 right-1/4 h-4 w-4 -translate-y-2 rounded-full bg-white"
            ></three>
            <four
                class="planet animate-planet-1 absolute bottom-0 right-2/4 h-4 w-4 translate-y-2 rounded-full bg-white"
            ></four>

            <five
                class="planet animate-planet-1 absolute left-0 top-1/4 h-4 w-4 translate-x-2 rounded-full bg-white"
            ></five>
            <six
                class="planet animate-planet-1 absolute left-0 top-2/4 h-4 w-4 -translate-x-2 rounded-full bg-white"
            ></six>

            <seven
                class="planet animate-planet-1 absolute bottom-1/4 right-0 h-4 w-4 -translate-x-2 rounded-full bg-white"
            ></seven>
            <eight
                class="planet animate-planet-1 absolute bottom-2/4 right-0 h-4 w-4 translate-x-2 rounded-full bg-white"
            ></eight>
        </div>

        <!-- Orbit 6 -->
        <div
            class="animate-orbit-6 absolute h-[40vh] w-[40vh] rounded-full border-2 border-dashed border-white opacity-50"
        >
            <one
                class="planet animate-planet-1 absolute left-1/4 top-0 h-4 w-4 translate-y-2 rounded-full bg-white"
            ></one>
            <two
                class="planet animate-planet-1 absolute left-2/4 top-0 h-4 w-4 -translate-y-2 rounded-full bg-white"
            ></two>

            <three
                class="planet animate-planet-1 absolute bottom-0 right-1/4 h-4 w-4 -translate-y-2 rounded-full bg-white"
            ></three>
            <four
                class="planet animate-planet-1 absolute bottom-0 right-2/4 h-4 w-4 translate-y-2 rounded-full bg-white"
            ></four>

            <five
                class="planet animate-planet-1 absolute left-0 top-1/4 h-4 w-4 translate-x-2 rounded-full bg-white"
            ></five>
            <six
                class="planet animate-planet-1 absolute left-0 top-2/4 h-4 w-4 -translate-x-2 rounded-full bg-white"
            ></six>

            <seven
                class="planet animate-planet-1 absolute bottom-1/4 right-0 h-4 w-4 -translate-x-2 rounded-full bg-white"
            ></seven>
            <eight
                class="planet animate-planet-1 absolute bottom-2/4 right-0 h-4 w-4 translate-x-2 rounded-full bg-white"
            ></eight>
        </div>

        <!-- Orbit 7 -->
        <div
            class="animate-orbit-7 absolute h-[45vh] w-[45vh] rounded-full border-2 border-dashed border-white opacity-40"
        >
            <one
                class="planet animate-planet-1 absolute left-1/4 top-0 h-4 w-4 translate-y-2 rounded-full bg-white"
            ></one>
            <two
                class="planet animate-planet-1 absolute left-2/4 top-0 h-4 w-4 -translate-y-2 rounded-full bg-white"
            ></two>

            <three
                class="planet animate-planet-1 absolute bottom-0 right-1/4 h-4 w-4 -translate-y-2 rounded-full bg-white"
            ></three>
            <four
                class="planet animate-planet-1 absolute bottom-0 right-2/4 h-4 w-4 translate-y-2 rounded-full bg-white"
            ></four>

            <five
                class="planet animate-planet-1 absolute left-0 top-1/4 h-4 w-4 translate-x-2 rounded-full bg-white"
            ></five>
            <six
                class="planet animate-planet-1 absolute left-0 top-2/4 h-4 w-4 -translate-x-2 rounded-full bg-white"
            ></six>

            <seven
                class="planet animate-planet-1 absolute bottom-1/4 right-0 h-4 w-4 -translate-x-2 rounded-full bg-white"
            ></seven>
            <eight
                class="planet animate-planet-1 absolute bottom-2/4 right-0 h-4 w-4 translate-x-2 rounded-full bg-white"
            ></eight>
        </div>
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
