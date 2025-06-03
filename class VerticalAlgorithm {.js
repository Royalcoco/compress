class VerticalAlgorithm {
    constructor() {
        this.layers = [];
    }

    addLayer(processFunction) {
        this.layers.push(processFunction);
    }

    process(input) {
        let currentOutput = input;

        // Traitement descendant
        for (let layer of this.layers) {
            currentOutput = layer(currentOutput);
        }

        // Révision ascendante
        for (let i = this.layers.length - 1; i >= 0; i--) {
            currentOutput = this.layers[i](currentOutput, true); // Mode révision
        }

        return currentOutput;
    }
}

// Exemple d'utilisation
const algorithm = new VerticalAlgorithm();

// Ajouter des couches
algorithm.addLayer((data, isRevision = false) => {
    return isRevision ? data - 1 : data * 2; // Traitement bidirectionnel
});
algorithm.addLayer((data, isRevision = false) => {
    return isRevision ? data / 2 : data + 3;
});

// Lancer le processus
const result = algorithm.process(5);
console.log("Résultat final :", result);

