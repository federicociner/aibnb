export const formatListings = (listings = []) =>
    listings.map(
        ({
            availability_365,
            compound,
            zipcode,
            review_scores_rating,
            ...listing
        }) => ({
            availability_365: ((Number(availability_365) / 365) * 100).toFixed(
                0
            ),
            compound: compound ? (Number(compound) * 10).toFixed(1) : undefined,
            zipcode: Number(zipcode)
                .toFixed(0)
                .toString(),
            review_scores_rating: (
                (Number(review_scores_rating) / 100) *
                5
            ).toFixed(1),
            ...listing
        })
    );
