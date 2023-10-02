


class SentenceContinue:

    @paddle.no_grad()
    def _generate_continue(self, sequences, model, tokenizer):
        for i, sequence in enumerate(sequences):
            augmented_sequence = []
            for ii in range(self.create_n):
                continue_sequence = (
                    generated_sequences[i * self.create_n + ii].replace(" ", "").replace("\n", "").replace("\t", "")
                )
                augmented_sequence.append(sequence + continue_sequence)
            augmented_sequences.append(augmented_sequence)
        return augmented_sequences