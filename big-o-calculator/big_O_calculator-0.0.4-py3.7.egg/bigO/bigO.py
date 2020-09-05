import math
import warnings
from random import randrange
from time import time
from typing import Any, Callable, List, Tuple

from win10toast import ToastNotifier


class bigO:
    """Big-O calculator

    usage:
        from bigO import bigO
        bigO = bigO.bigO()
        bigO.test(someSort, "random")
    """

    def __init__(self):
        self.coef = 0.0
        self.rms = 0.0
        self.cplx = 0
        self.O1 = 1
        self.ON = 2
        self.ON2 = 3
        self.ON3 = 4
        self.OLogN = 5
        self.ONLogN = 6
        self.OLambda = 7
        self.fitCurves = [self.O1, self.ON, self.ON2, self.ON3, self.OLogN, self.ONLogN]

    def str(self):
        return self.complexity2str(self.cplx)

    def complexity2str(self, cplx: int) -> str:
        def switch(cplx):
            return {
                self.ON: "O(n)",
                self.ON2: "O(n^2)",
                self.ON3: "O(n^3)",
                self.OLogN: "O(log(n)",
                self.ONLogN: "O(nlog(n))",
                self.O1: "O(1)",
            }.get(cplx, "f(n)")

        return switch(cplx)

    def fittingCurve(self, cplx: int) -> Callable:
        def bigO_ON(n):
            return n

        def bigO_ON2(n):
            return n * n

        def bigO_ON3(n):
            return n * n * n

        def bigO_OLogN(n):
            return math.log2(n)

        def bigO_ONLogN(n):
            return n * math.log2(n)

        def bigO_O1(_):
            return 1.0

        def switch(cplx):
            return {
                self.O1: bigO_O1,
                self.ON: bigO_ON,
                self.ON2: bigO_ON2,
                self.ON3: bigO_ON3,
                self.OLogN: bigO_OLogN,
                self.ONLogN: bigO_ONLogN,
            }.get(cplx, bigO_O1)

        return switch(cplx)

    def minimalLeastSq(self, arr: List[Any], times: float, function: Callable):
        # sigmaGn = 0.0
        sigmaGnSquared = 0.0
        sigmaTime = 0.0
        sigmaTimeGn = 0.0

        floatN = float(len(arr))

        for i in range(len(arr)):
            gnI = function(arr[i])
            # sigmaGn = gnI
            sigmaGnSquared += gnI * gnI
            sigmaTime += times[i]
            sigmaTimeGn += times[i] * gnI

        result = bigO()
        result.cplx = self.OLambda

        result.coef = sigmaTimeGn / sigmaGnSquared

        rms = 0.0
        for i in range(len(arr)):
            fit = result.coef * function(arr[i])
            rms += math.pow(times[i] - fit, 2)

        mean = sigmaTime / floatN
        result.rms = math.sqrt(rms / floatN) / mean

        return result

    def estimate(self, n: List[int], times: List[float]):
        assert len(n) == len(
            times
        ), f"ERROR: Length mismatch between N:{len(n)} and TIMES:{len(times)}."
        assert len(n) >= 2, "ERROR: Need at least 2 runs."

        bestFit = bigO()

        # assume that O1 is the best case
        bestFit = self.minimalLeastSq(n, times, self.fittingCurve(self.O1))
        bestFit.cplx = self.O1

        for fit in self.fitCurves:
            currentFit = self.minimalLeastSq(n, times, self.fittingCurve(fit))
            if currentFit.rms < bestFit.rms:
                bestFit = currentFit
                bestFit.cplx = fit

        return bestFit

    def test(self, functionName: Callable, array: str) -> Tuple[str, List[Any]]:
        """Big-O calculator

        Args:
            functionName (Callable): a function to call |
            array (string): "random", "sorted", "reversed", "partial", "Ksorted"

        Returns:
            complexity (string) : ex) O(N)
            _ (string) : Error message else None
            result (array) : Result of sorted array

        """
        # TODO : "all" to test all types of array
        def genRandomArray(size):
            array = []
            for _ in range(size):
                array.append(randrange(-size, size))
            return array

        def genSortedArray(size):
            array = []
            for value in range(size):
                array.append(value)
            return array

        def genReversedArray(size):
            array = []
            for value in reversed(range(size)):
                array.append(value)
            return array

        def genPartialArray(size):
            array = genRandomArray(size)
            sorted_array = genSortedArray(size)

            array[size // 4 : size // 2] = sorted_array[size // 4 : size // 2]
            return array

        def genKsortedArray(size, k):
            def reverseRange(array, a, b):
                i = a
                j = b - 1
                while i < j:
                    array[i], array[j] = array[j], array[i]
                    i += 1
                    j -= 1

                return array

            # ? can return random array
            assert size > k, "K must be smaller than the size."
            if size == 0:
                return genSortedArray(size)
            elif size == k:
                return genReversedArray(size)

            array = []
            for value in range(-size // 2, size // 2):
                array.append(value)

            right = randrange(k)
            while right > size - k - 1:  # Don't reverse again
                right -= 1

            if size != k:
                k += 1

            reverseRange(array, 0, k)
            reverseRange(array, len(array) - right, len(array))

            return array

        bigOtest = bigO()

        sizes = [10, 100, 1000, 10000, 100000]
        maxIter = 5
        times = []
        result = []

        toaster = ToastNotifier()
        print(f"Running {functionName.__name__}({array} array)...")
        toaster.show_toast(
            "Big-O Caculator",
            f"Running {functionName.__name__}({array} array)...",
            duration=2,
        )

        for size in sizes:
            timeTaken = 0.0
            nums = []

            if array == "random":
                nums = genRandomArray(size)
            elif array == "sorted":
                nums = genSortedArray(size)
            elif array == "partial":
                nums = genPartialArray(size)
            elif array == "reversed":
                nums = genReversedArray(size)
            elif array.lower() == "Ksorted":
                nums = genKsortedArray(size, size // 10)
            # elif array == "custom":
            #    nums = custom
            #    assert len(nums) != 0, "Please, pass the custom array you want.
            else:  # default = random array
                nums = genRandomArray(size)

            currentIter = 0

            while currentIter < maxIter:
                start = time()
                result = functionName(nums)
                end = time()
                timeTaken += end - start
                currentIter += 1

                if result == None:
                    warnings.warn(
                        "Please, return the array to see result.", UserWarning
                    )
                else:
                    assert result == sorted(
                        nums
                    ), "This function doesn't sort correctly."

            timeTaken /= maxIter
            times.append(timeTaken)

        complexity = bigOtest.estimate(sizes, times)
        print(f"Completed {functionName.__name__}({array} array): {complexity.str()}")
        print(f"Time took: {sum(times):.5f}s")
        toaster.show_toast(
            "Big-O Caculator",
            f"Completed {functionName.__name__}({array} array): {complexity.str()}",
            duration=3,
        )

        return complexity.str(), result
