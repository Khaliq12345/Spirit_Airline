from fastapi import FastAPI
import json
import requests
import pandas as pd

app = FastAPI()

@app.get("/{orig}")
async def get_data(orig: str, dest: str, month: int, year: int, day: int):
    item_list = []
    url = "https://www.travelocity.com/graphql"
    payload = {
        "operationName": "FlightsShoppingPwaFlightSearchResultsFlightsSearch",
        "query": """
            query FlightsShoppingPwaFlightSearchResultsFlightsSearch(
    $context: ContextInput!
    $flightsSearchContext: FlightsSearchContextInput
    $journeyCriteria: [FlightsJourneyCriteriaInput!]!
    $queryState: FlightsQueryState
    $searchFilterValuesList: [FlightsSearchFilterValuesInput!]
    $searchPreferences: FlightsSearchPreferencesInput
    $sortOption: FlightsSortOptionTypeInput
    $rewardsOption: RewardsOption
    $travelerDetails: [FlightsTravelerDetailsInput!]
    $searchPagination: PaginationInput
    $shoppingContext: ShoppingContextInput
    $faresSeparationType: FlightsFaresSeparationType
    $flightsSearchComponentCriteria: FlightsSearchComponentCriteriaInput
    $fareCalendarPrice: String
    $flightsDisplayComponentValues: FlightsDisplayComponentValuesInput
    $virtualAgentContext: VirtualAgentContextInput
    ) {
    flightsSearch(
        context: $context
        flightsSearchContext: $flightsSearchContext
        journeyCriteria: $journeyCriteria
        queryState: $queryState
        searchFilterValuesList: $searchFilterValuesList
        searchPreferences: $searchPreferences
        sortOption: $sortOption
        rewardsOption: $rewardsOption
        travelerDetails: $travelerDetails
        searchPagination: $searchPagination
        shoppingContext: $shoppingContext
        faresSeparationType: $faresSeparationType
        flightsSearchComponentCriteria: $flightsSearchComponentCriteria
        fareCalendarPrice: $fareCalendarPrice
        flightsDisplayComponentValues: $flightsDisplayComponentValues
        virtualAgentContext: $virtualAgentContext
    ) {
        clientMetadata {
        ... on FlightsPWAMetadata {
            pageName
            pageNameAnalytics {
            ...FlightsAnalytics
            }
            responseTags
            responseMetrics {
            name
            value
            }
        }
        }
        failedRequestMessaging {
        icon {
            description
            id
        }
        message
        action {
            ...FlightAction
        }
        errorRecoveryButtons {
            ...FlightAction
        }
        title
        }
        noListingMessaging {
        ... on FlightsNoFlightsFoundMessaging {
            __typename
            icon {
            id
            description
            }
            message
            title
        }
        ... on FlightsNoFlightsFoundWithFilterMessaging {
            __typename
            icon {
            id
            description
            }
            message
            clearFiltersAction {
            ...FlightAction
            }
            title
        }
        ... on FlightsActionableErrorMessaging {
            __typename
            icon {
            description
            id
            }
            message
            action {
            ...FlightAction
            }
            errorRecoveryButtons {
            ...FlightAction
            }
            title
        }
        ... on FlightsSmartNoFlightsFoundMessaging {
            __typename
            alternateAirportOptions {
            ...AlternateAirportOptions
            }
            alternateDateOptions {
            ...AlternateDateOptions
            }
            editSearchButton {
            ...FlightAction
            }
            flightsDisplayComponentCountingValue {
            ...FlightsDisplayComponentCountingValue
            }
            icon {
            ...IconSearch
            }
            message
            title
        }
        }
        sortAndFilterResult {
        ... on FlightsLoadedSortAndFilterResult {
            title
            filterAnalyticsList {
            ...FlightsAnalytics
            }
            appliedFiltersSummary {
            appliedFilters {
                analytics {
                ...FlightsAnalytics
                }
                dismissIcon {
                description
                id
                }
                label
                identifier
                nextSearchSortFilterCriteria {
                filterCriteria {
                    arrivalAirportCodeFilterValue {
                    airportCode
                    }
                    arrivalTimeFilterValue {
                    timeOfDay
                    }
                    departureAirportCodeFilterValue {
                    airportCode
                    }
                    departureTimeFilterValue {
                    timeOfDay
                    }
                    durationFilterValue {
                    maxDuration
                    }
                    numOfStopFilterValue {
                    stopInfo {
                        numberOfStops
                        stopFilterOperation
                    }
                    }
                    preferredAirlineFilterValue {
                    carrierCode
                    }
                    flexibleChangePolicyBasedFilterValue {
                    policyName
                    }
                    seatChoiceBasedFilterValue {
                    seatChoice
                    }
                    carryOnBagBasedFilterValue {
                    carryOnBag
                    }
                    checkedBagBasedFilterValue {
                    numOfCheckedBags
                    }
                    noCancelFeeBasedFilterValue {
                    noCancelFee
                    }
                    creditEligibleFilterValue {
                    creditEligible
                    }
                }
                }
                accessibilityMessage
                dismissIconAccessibility
            }
            }
            applyAction {
            accessibility {
                onCompletion
                usage
            }
            analytics {
                ...FlightsAnalytics
            }
            details
            label
            }
            clearSelectionLabel {
            label
            analytics {
                ...FlightsAnalytics
            }
            accessibility {
                onCompletion
                usage
            }
            }
            clearAllSelectionLabel {
            label
            analytics {
                ...FlightsAnalytics
            }
            accessibility {
                onCompletion
                usage
            }
            }
            dismiss {
            description
            id
            }
            dismissAnalytics {
            ...FlightsAnalytics
            }
            revealAction {
            accessibility {
                onCompletion
                usage
            }
            appliedFilterCount
            iconAndLabel {
                icon {
                description
                id
                }
                label
            }
            enabled
            }
            revealActionAnalytics {
            ...FlightsAnalytics
            }
            sortPresentation {
            __typename
            label
            options {
                accessibility {
                onCompletion
                usage
                }
                analytics {
                ...FlightsAnalytics
                }
                label
                sortType {
                sortOrder
                sortType
                }
            }
            selectedOption {
                label
                sortType {
                sortOrder
                sortType
                }
            }
            selectionActive
            }
            filterPresentation {
            __typename
            accessibility {
                onCompletion
                usage
            }
            eventAnalytics {
                ...FlightsFiltersEventAnalytics
            }
            options {
                __typename
                ... on FlightsListDisplayFilterOption {
                items {
                    ...FlightsListDisplayFilterItem
                }
                itemsDefaultDisplayCount
                label
                priceFromLabel
                showMoreToggle {
                    ...FlightsToggleSearch
                }
                supportsMultipleSelection
                type
                }
                ... on FlightsCardsDisplayFilterOption {
                items {
                    ...FlightsCardsDisplayFilterItem
                }
                label
                type
                supportsMultipleSelection
                }
            }
            title
            emptyFiltersMessage
            }
        }
        }
        listingResult {
        ... on FlightsLoadedListingResult {
            pinnedListingUnavailableMessage
            accessibilityMessage
            appliedFilterAccessibility
            showMoreListingLoadedAccessibilityMessage
            appliedSortingAccessibility
            listings {
            __typename
            ...FlightsSuggestedFilterMessageListing
            ...FlightsStandardOffer
            ...FlightsBargainFareOffer
            ...FlightsFeedback
            ...FlightsCrossSellMessage
            ...FlightsCrossSellOffer
            ...FlightsCouponCredit
            ...FlightsSustainabilityMessage
            ...FlightsCreditsAvailableListing
            ...FlightsEGDSElementWrapper
            ...FlightsListingMessagingCard
            }
            flightsListingsAnalytics {
            onViewedAnalytics {
                ...FlightsAnalytics
            }
            onViewedAnalyticsList {
                ...FlightsAnalytics
            }
            pinnedListingDisplayedAnalytics {
                ...FlightsAnalytics
            }
            moreListingsDisplayedAnalytics {
                ...FlightsAnalytics
            }
            moreListingsErrorAnalytics {
                ...FlightsAnalytics
            }
            moreListingsLoadTimeAnalytics {
                ...FlightsAnalytics
            }
            fareCalendarAnalytics {
                ...FlightsAnalytics
            }
            fareUpsellPercentageAnalytics {
                ...FlightsAnalytics
            }
            bestBetsDisplayedAnalytics {
                ...FlightsAnalytics
            }
            bestSortDisplayedAnalytics {
                ...FlightsAnalytics
            }
            }
            listingsAction {
            ...FlightAction
            }
            moreListingsAvailable
        }
        }
        flightsOpinionLab {
        ... on FlightsActionAndLabel {
            label
            selectAction {
            ...FlightAction
            }
        }
        }
        rewardsPricingInfo {
        ...FlightsRewardsPricingInfo
        }
        pageTitle {
        ...PageTitle
        }
        dialogs {
        __typename
        ... on FlightsDialogStandard {
            actions {
            ...FlightAction
            }
            animation
            displayedAnalytics {
            ...FlightsAnalytics
            }
            title
            header
            message
        }
        ... on FlightsDialogStaleSession {
            actions {
            ...FlightAction
            }
            animation
            displayedAnalytics {
            ...FlightsAnalytics
            }
            header
            message
            timeoutInSeconds
        }
        ... on FlightsForcedChoiceCrossSellDialog {
            actions {
            ...FlightAction
            }
            animation
            annotation {
            completeText
            items {
                styles
                text
                __typename
                ... on FlightsPhraseLinkNode {
                analytics {
                    ...FlightsAnalytics
                }
                link
                }
            }
            }
            header
            messageBody {
            __typename
            ... on EGDSPlainText {
                __typename
                text
            }
            ... on EGDSGraphicText {
                __typename
                graphic {
                ...UIGraphicFragment
                }
                text
            }
            }
            message
            displayCounter
            hotelDatesTitle
            displayedAnalytics {
            ...FlightsAnalytics
            }
            displayBlockedAnalytics {
            ...FlightsAnalytics
            }
            checkInDate {
            ...HotelsDate
            }
            checkOutDate {
            ...HotelsDate
            }
        }
        }
        banners {
        ...FlightsIconPlacard
        }
        allBanners {
        ...FlightsIconPlacard
        }
        cheapestListingInfo {
        price
        analytics {
            ...FlightsAnalytics
        }
        nffAnalytics {
            ...FlightsAnalytics
        }
        deviationAnalytics {
            ...FlightsAnalytics
        }
        }
        gaiaId
        stepIndicator {
        ...FlightsStepIndicator
        }
        flightsReviewLoadingElements {
        freeCancellation {
            ... on FlightsImagePlacard {
            __typename
            image {
                url
                description
            }
            heading
            message
            }
        }
        flightsJourneyReviewCommon {
            changeFlight {
            ...FlightAction
            }
            fareSummarySkeletonCount
            flightSummarySkeletonCount
        }
        clientMetaData {
            ...ClientMetaData
        }
        pageTitle {
            ...PageTitle
        }
        priceSummary {
            __typename
            ... on FlightsLoadingPriceSummary {
            title
            skeletonCount
            tripTotalLabel
            buttonAction {
                ...FlightAction
            }
            }
        }
        }
        shoppingContext {
        multiItem {
            id
            packageType
        }
        }
        listingsHeaderPlacards {
        ...FlightsMessagingCardPlacardFragment
        }
    }
    }

    fragment FlightsCardsDisplayFilterItem on FlightsCardsDisplayFilterItem {
    accessibility {
        onCompletion
        usage
    }
    card {
        id
        description
    }
    deselectAnalytics {
        ...FlightsAnalytics
    }
    flightsSearchFilterValues {
        arrivalAirportCodeFilterValue {
        airportCode
        }
        arrivalTimeFilterValue {
        timeOfDay
        }
        departureAirportCodeFilterValue {
        airportCode
        }
        departureTimeFilterValue {
        timeOfDay
        }
        durationFilterValue {
        maxDuration
        }
        numOfStopFilterValue {
        stopInfo {
            stopFilterOperation
            numberOfStops
        }
        }
        preferredAirlineFilterValue {
        carrierCode
        }
        flexibleChangePolicyBasedFilterValue {
        policyName
        }
        seatChoiceBasedFilterValue {
        seatChoice
        }
        carryOnBagBasedFilterValue {
        carryOnBag
        }
        checkedBagBasedFilterValue {
        numOfCheckedBags
        }
        noCancelFeeBasedFilterValue {
        noCancelFee
        }
        creditEligibleFilterValue {
        creditEligible
        }
    }
    label
    identifier
    subLabel
    selectAnalytics {
        ...FlightsAnalytics
    }
    selected
    value {
        __typename
        ... on FlightsAirportCodeFilterValue {
        airportCode
        }
        ... on FlightsDurationBasedFilterValue {
        maxDuration
        }
        ... on FlightsPreferredAirlineFilterValue {
        carrierCode
        }
        ... on FlightsFlexibleChangePolicyBasedFilterValue {
        policyName
        }
        ... on FlightsSeatChoiceBasedFilterValue {
        seatChoice
        }
        ... on FlightsCarryOnBagBasedFilterValue {
        carryOnBag
        }
        ... on FlightsCheckedBagBasedFilterValue {
        numOfCheckedBags
        }
        ... on FlightsNoCancelFeeBasedFilterValue {
        noCancelFee
        }
        ... on FlightsStopBasedFilterValue {
        stopInfo {
            stopFilterOperation
            numberOfStops
        }
        }
        ... on FlightsTimeBasedFilterValue {
        timeOfDay
        }
        ... on FlightsCreditEligibleFilterValue {
        creditEligible
        }
    }
    }

    fragment FlightsListDisplayFilterItem on FlightsListDisplayFilterItem {
    selectPositionAnalytics {
        ...FlightsAnalytics
    }
    analytics {
        ...FlightsFilterItemAnalytics
    }
    accessibility {
        onCompletion
        usage
    }
    deselectAnalytics {
        ...FlightsAnalytics
    }
    flightsSearchFilterValues {
        arrivalAirportCodeFilterValue {
        airportCode
        }
        arrivalTimeFilterValue {
        timeOfDay
        }
        departureAirportCodeFilterValue {
        airportCode
        }
        departureTimeFilterValue {
        timeOfDay
        }
        durationFilterValue {
        maxDuration
        }
        numOfStopFilterValue {
        stopInfo {
            stopFilterOperation
            numberOfStops
        }
        }
        preferredAirlineFilterValue {
        carrierCode
        }
        flexibleChangePolicyBasedFilterValue {
        policyName
        }
        seatChoiceBasedFilterValue {
        seatChoice
        }
        carryOnBagBasedFilterValue {
        carryOnBag
        }
        checkedBagBasedFilterValue {
        numOfCheckedBags
        }
        noCancelFeeBasedFilterValue {
        noCancelFee
        }
        creditEligibleFilterValue {
        creditEligible
        }
    }
    label
    identifier
    selectAnalytics {
        ...FlightsAnalytics
    }
    selected
    formattedMultiItemStartingPrice
    startingPrice {
        formatted
    }
    value {
        __typename
        ... on FlightsAirportCodeFilterValue {
        airportCode
        }
        ... on FlightsDurationBasedFilterValue {
        maxDuration
        }
        ... on FlightsPreferredAirlineFilterValue {
        carrierCode
        }
        ... on FlightsFlexibleChangePolicyBasedFilterValue {
        policyName
        }
        ... on FlightsSeatChoiceBasedFilterValue {
        seatChoice
        }
        ... on FlightsCarryOnBagBasedFilterValue {
        carryOnBag
        }
        ... on FlightsCheckedBagBasedFilterValue {
        numOfCheckedBags
        }
        ... on FlightsNoCancelFeeBasedFilterValue {
        noCancelFee
        }
        ... on FlightsStopBasedFilterValue {
        stopInfo {
            stopFilterOperation
            numberOfStops
        }
        }
        ... on FlightsTimeBasedFilterValue {
        timeOfDay
        }
        ... on FlightsCreditEligibleFilterValue {
        creditEligible
        }
    }
    }

    fragment FlightsBargainFareOffer on FlightsBargainFareOffer {
    bargainOfferAccessibilityMessage: accessibilityMessage
    accessibilityHeading
    bargainPricingInformation {
        priceLockup {
        ...PriceLockupFragment
        }
        cancellationMessage
        price {
        completeText
        items {
            styles
            text
            __typename
            ... on FlightsPhraseLinkNode {
            analytics {
                ...FlightsAnalytics
            }
            }
        }
        }
        mainPrice {
        completeText
        items {
            styles
            text
            __typename
            ... on FlightsPhraseLinkNode {
            analytics {
                ...FlightsAnalytics
            }
            }
        }
        }
        pricePerTraveler {
        completeText
        items {
            styles
            text
            __typename
            ... on FlightsPhraseLinkNode {
            analytics {
                ...FlightsAnalytics
            }
            }
        }
        }
        taxesLabel
        totalLabel
        totalPriceForAllTravelers {
        completeText
        items {
            styles
            text
            __typename
            ... on FlightsPhraseLinkNode {
            analytics {
                ...FlightsAnalytics
            }
            }
        }
        }
        tripType
        subText
    }
    description {
        completeText
        items {
        styles
        text
        __typename
        ... on FlightsPhraseLinkNode {
            analytics {
            ...FlightsAnalytics
            }
            link
        }
        }
    }
    header {
        completeText
        items {
        text
        styles
        __typename
        ... on FlightsPhraseLinkNode {
            link
            analytics {
            ...FlightsAnalytics
            }
        }
        }
    }
    image {
        url
    }
    journeys {
        __typename
        flightsJourneyAvailableFaresInformation {
        ...FlightsJourneyAvailableFares
        }
        flightsDetailsAndFaresPresentation {
        ...FlightsDetailsAndFaresPresentationFragment
        }
    }
    journeyContinuationId
    onClickAnalyticsList {
        ...FlightsAnalytics
    }
    }

    fragment FlightsSuggestedFilterMessageListing on FlightsSuggestedFilterMessageListing {
    __typename
    suggestedFilterDetails {
        __typename
        ... on FlightsImagePlacard {
        image {
            url
        }
        heading
        message
        actions {
            ... on FlightsAction {
            displayAction
            displayType
            type
            analytics {
                ...FlightsAnalytics
            }
            }
        }
        }
    }
    suggestedFilter {
        ... on FlightsSuggestedFilterItem {
        selected
        accessibility {
            usage
            onCompletion
        }
        identifier
        label
        value {
            ... on FlightsFlexibleChangePolicyBasedFilterValue {
            policyName
            }
        }
        type
        }
    }
    }

    fragment FlightsSustainabilityMessage on FlightsSustainabilityMessage {
    details {
        ...FlightsSustainabilityDialogDetails
    }
    information {
        ...FlightsIconPlacard
    }
    }

    fragment FlightsSustainabilityDialogDetails on FlightsSustainabilityDialogDetails {
    heading
    dismiss {
        ...FlightAction
    }
    closingText {
        ...FlightsTextSection
    }
    iconRow {
        ... on FlightsIconAndHeading {
        heading
        icons {
            ...FlightsIconAndLabel
        }
        }
    }
    introduction {
        ...FlightsPhrase
    }
    }

    fragment FlightsTextSection on FlightsTextSection {
    heading
    displayAnalytics {
        ...FlightsAnalytics
    }
    messages {
        ...FlightsPhrase
    }
    }

    fragment FlightsFeedback on FlightsFeedback {
    __typename
    feedbackLinkAction {
        ...FlightAction
    }
    iconAndLabel {
        icon {
        description
        id
        }
        label
        accessibility
    }
    }

    fragment FlightsCouponCredit on FlightsCouponCredit {
    couponCreditAction {
        ...FlightAction
    }
    imageListingLabel {
        ...FlightsImageListingLabel
    }
    }

    fragment FlightsImageListingLabel on FlightsImageListingLabel {
    image {
        url
    }
    label
    subLabel
    }

    fragment MultiItemSearchContext on MultiItemSearchContext {
    flights {
        primary {
        journeyCriterias {
            departureDate {
            day
            month
            year
            }
            origin
            destination
        }
        searchPreferences {
            cabinClass
            advancedFilters
        }
        tripType
        travelers {
            age
            type
        }
        }
    }
    }

    fragment FlightsEGDSElementWrapper on EGDSElementWrapper {
    element {
        ...EgdsTextFragment
    }
    }

    fragment FlightsCrossSellMessage on FlightsCrossSellMessage {
    __typename
    multiItemFlightCrossSellPrimer {
        flightCrossSellProductType
        multiItemSearchContext {
        ...MultiItemSearchContext
        }
    }
    }

    fragment FlightsStandardOffer on FlightsStandardOffer {
    __typename
    accessibilityHeading
    accessibilityMessage
    pinnedOfferMessage
    badges {
        accessibilityMessage
        icon {
        description
        id
        }
        text
        type
    }
    journeys {
        __typename
        airlines {
        image {
            url
            description
        }
        text
        }
        cabinClass
        departureAndArrivalTime {
        completeText
        items {
            styles
            text
        }
        }
        departureAndArrivalLocations
        layoverInformation
        differentDayArrival
        differentDayArrivalAccessibilityMessage
        displayAction {
        id
        description
        }
        durationAndStops
        flightOperatedBy
        label
        urgencyMessage
        urgencyAccessibilityMessage
        flightsJourneyAvailableFaresInformation {
        ...FlightsJourneyAvailableFares
        }
        flightsDetailsAndFaresPresentation {
        ...FlightsDetailsAndFaresPresentationFragment
        }
        hygieneAmenitiesMessage
        adjustedStayDatesMessage {
        ...FlightsIconPhrases
        }
        positiveHighlightsMessage
        restrictiveAmenityIcons {
        ...IconSearch
        }
        highlightRelevantFaresAnalytics {
        ...FlightsAnalytics
        }
    }
    pricingInformation {
        loyaltyEarnMessage {
        ...FlightsMarkAndLabel
        }
        partnerLoyaltyEarnMessage {
        ...FlightsMarkAndLabel
        }
        loyaltyPointsOption {
        ...FlightsLoyaltyPointsOption
        }
        price {
        completeText
        items {
            text
            styles
        }
        }
        mainPrice {
        completeText
        items {
            text
            styles
        }
        }
        subPrice {
        completeText
        items {
            text
            styles
        }
        }
        pricePerTraveler {
        completeText
        items {
            text
            styles
        }
        }
        taxesLabel
        totalLabel
        totalPriceForAllTravelers {
        completeText
        items {
            text
            styles
        }
        }
        subText
        tripType
        priceLockup {
        ...PriceLockupFragment
        }
        subTexts {
        text
        ... on EGDSStylizedText {
            theme
        }
        }
    }
    restrictiveFareRules {
        dismissLabel
        displayAction {
        icon {
            id
            description
        }
        label {
            completeText
            items {
            styles
            text
            }
        }
        }
        rules
        title
    }
    specialFareType
    sponsoredAirline {
        airlineCode
        adUnitID
        advertiserID
        creativeID
        clickTrackingURL
        delayedImpressionURL
        orderID
        sponsoredHeader
        sponsoredText
    }
    tag {
        image {
        description
        url
        }
        message
    }
    flightsOfferAnalytics {
        onViewedAnalyticsList {
        ...FlightsAnalytics
        }
    }
    journeyContinuationId
    onClickAnalyticsList {
        ...FlightsAnalytics
    }
    sponsoredUpsell {
        ...FlightsOfferSponsoredUpsell
    }
    }

    fragment FlightsCreditsAvailableListing on FlightsCreditsAvailableListing {
    immediateDialogAction {
        accessibility
        analytics {
        ...ClientSideAnalytics
        }
        dialog {
        closeAnalytics {
            ...ClientSideAnalytics
        }
        }
        dialogContents {
        egdsElementId
        }
    }
    messagingCardPlacard {
        __typename
        button {
        ...FlightsActionButton
        }
        displayType
        messagingCard {
        ...UIMessagingCard
        }
        onViewedAnalytics {
        ...FlightsAnalytics
        }
    }
    toastNotification {
        __typename
        egdsElementId
        text
    }
    }

    fragment FlightsActionButton on FlightsActionButton {
    __typename
    accessibility
    clientAction {
        __typename
        accessibility
        analyticsList {
        ...ClientSideAnalytics
        }
        ...FlightsBoundNavigation
        ...FlightsCreditSelectorOpenAction
        ...FlightsNavigateToDetails
        ...FlightsResourceLinkAction
        ...FlightsSelectionAction
        ...MultiItemSelectPackage
        ...MultiItemSelectProducts
    }
    disabled
    egdsElementId
    icon {
        ...IconSearch
    }
    primary
    style
    buttonStyle: style
    action {
        __typename
        accessibility
        analytics {
        ...ClientSideAnalytics
        }
    }
    }

    fragment FlightsResourceLinkAction on FlightsResourceLinkAction {
    __typename
    accessibility
    analyticsList {
        ...ClientSideAnalytics
    }
    resource {
        ...HttpURI
    }
    }

    fragment HttpURI on HttpURI {
    __typename
    relativePath
    value
    }

    fragment FlightsCreditSelectorOpenAction on FlightsCreditSelectorOpenAction {
    __typename
    accessibility
    analyticsList {
        ...ClientSideAnalytics
    }
    }

    fragment FlightsSelectionAction on FlightsSelectionAction {
    value
    }

    fragment FlightsBoundNavigation on FlightsBoundNavigation {
    jcid
    mipt
    pageId
    stepIndicatorJcid
    }

    fragment FlightsNavigateToDetails on FlightsNavigateToDetails {
    dialogId
    nextPage {
        ...HttpURI
    }
    packagesUrl {
        ...HttpURI
    }
    }

    fragment MultiItemSelectProducts on MultiItemSelectProducts {
    flightsOfferNaturalKeys {
        ...FlightsOfferNaturalKeysFragment
    }
    multiItemPriceToken
    multiItemSessionId
    }

    fragment MultiItemSelectPackage on MultiItemSelectPackage {
    packageOfferId
    }

    fragment UIMessagingCard on UIMessagingCard {
    __typename
    egdsElementId
    graphic {
        ...UIGraphicFragment
    }
    primary
    secondaries
    }

    fragment ClientSideAnalytics on ClientSideAnalytics {
    linkName
    referrerId
    uisPrimeMessages {
        messageContent
        schemaName
    }
    }

    fragment FlightsLoyaltyPointsOption on FlightsLoyaltyPointsOption {
    overageAmount
    strikeThroughFormattedPoints
    leadingCaption
    formattedPoints
    isPointsFirst
    isStrikeThroughFirst
    accessibility
    }

    fragment FlightsMarkAndLabel on FlightsMarkAndLabel {
    accessibility
    label
    subLabel
    mark {
        id
        description
    }
    stylisedText {
        ...EGDSSpannableTextFragment
    }
    }

    fragment FlightsToggleSearch on FlightsToggle {
    __typename
    collapseActionable {
        ...TogglePhaseSearch
    }
    expandActionable {
        ...TogglePhaseSearch
    }
    expanded
    }

    fragment IconSearch on Icon {
    __typename
    description
    id
    size
    withBackground
    theme
    title
    }

    fragment TogglePhaseSearch on TogglePhase {
    __typename
    accessibilityMessage
    action
    analytics {
        ...FlightsAnalytics
    }
    icon {
        ...IconSearch
    }
    }

    fragment FlightsAnalytics on FlightsAnalytics {
    __typename
    linkName
    referrerId
    }

    fragment FlightsIconPlacard on FlightsIconPlacard {
    __typename
    heading
    message
    icon {
        description
        id
        size
        withBackground
    }
    actions {
        ...FlightAction
    }
    displayType
    }

    fragment FlightAction on FlightsAction {
    __typename
    accessibilityMessage
    analytics {
        ...FlightsAnalytics
    }
    analyticsList {
        ...FlightsAnalytics
    }
    displayAnalytics {
        ...FlightsAnalytics
    }
    displayAction
    displayType
    accessibilityActionMessage {
        usage
        onCompletion
    }
    icon {
        ...IconSearch
    }
    journeySearchCriteria {
        previousFlightSelections {
        journeyIndex
        offerIdentifier
        }
        journeyCriteria {
        destination
        departureDate {
            day
            month
            year
        }
        origin
        }
        searchPreferences {
        cabinClass
        }
    }
    relativeURI {
        relativePath
        value
    }
    relativePackageableURI {
        relativePath
        value
    }
    stepIndicator {
        ...FlightsStepIndicator
    }
    searchPagination {
        ...Pagination
    }
    type
    }

    fragment FlightsStepIndicator on FlightsStepIndicator {
    errorAnalytics {
        ...FlightsAnalytics
    }
    journeyContinuationId
    }

    fragment CoordinateInformationSearch on CoordinateInformation {
    icon {
        ...IconSearch
    }
    flightDetailsWarningInfo {
        ...FlightsIconAndLabel
    }
    subtitle
    titleAndAccessibilityMessage {
        accessibilityMessage
        text
    }
    }

    fragment FlightsJourneyAvailableFares on FlightsJourneyAvailableFares {
    __typename
    applySelection {
        ...FlightAction
    }
    dismissDetailedJourneyInformation {
        ...FlightsActionableIcon
    }
    fareChoiceInformation {
        __typename
        accessibleHeading
        availableFaresCount
        defaultBaggageInformation {
        bagFeesMoreInfo {
            __typename
            completeText
            delimeter
            items {
            styles
            text
            ... on FlightsPhraseLinkNode {
                accessibility
                analytics {
                ...FlightsAnalytics
                }
                icon
                link
            }
            }
        }
        defaultBagSelectionMessage
        details {
            baggageDetail
            topic
        }
        dismissAction
        displayDetailsAction
        label
        displayAnalyticsItems {
            ...FlightsAnalytics
        }
        }
        displayAnalytics {
        ...FlightsAnalytics
        }
        errorAnalytics {
        ...FlightsAnalytics
        }
        scrollAnalytics {
        ...FlightsAnalytics
        }
        convertAnalytics {
        ...FlightsAnalytics
        }
        fares {
        __typename
        accessibilityMessage
        safetyLocationAccessibilityMessage
        selectFareActionAltText
        multiItemPriceToken
        multiItemAction {
            __typename
            ... on MultiItemSelectPackageAction {
            packageOfferId
            }
            ... on MultiItemSelectProductsAction {
            multiItemSessionId
            flightsOfferNaturalKeys {
                ...FlightsOfferNaturalKeysFragment
            }
            multiItemPriceToken
            }
        }
        flightsOfferNaturalKeys {
            ...FlightsOfferNaturalKeysFragment
        }
        baggageFeesInformation {
            __typename
            bagFeesMoreInfo {
            __typename
            completeText
            delimeter
            items {
                __typename
                styles
                text
                ... on FlightsPhraseLinkNode {
                accessibility
                analytics {
                    ...FlightsAnalytics
                }
                icon
                link
                }
            }
            }
            defaultBagSelectionMessage
            details {
            __typename
            baggageDetail
            topic
            }
            displayDetailsAction
            dismissAction
            label
            displayAnalyticsItems {
            ...FlightsAnalytics
            }
        }
        cabinClass
        cabinClassAndBookingCodes
        selectFareAction {
            ...FlightAction
        }
        clickEventAnalytics {
            ...FlightsAnalytics
        }
        collapsedRules {
            ...FlightsJourneyAmenities
        }
        expandedRules {
            ...FlightsJourneyAmenitiesWithLabel
        }
        amenityHierarchyRules {
            ...FlightsJourneyAmenitiesWithLabel
        }
        amenityRules {
            __typename
            amenities {
            ...FlightsIconAndLabel
            }
            itemsDefaultDisplayCount
        }
        changeCancellationMessages {
            __typename
            displayAnalyticsList {
            ...FlightsAnalytics
            }
            heading
            messages {
            ...FlightsPhrase
            }
        }
        chooseFareAction {
            __typename
            accessibilityMessage
            displayAction
            type
        }
        fareScrollAnalytics {
            ...FlightsAnalytics
        }
        loyaltyPointsOption {
            ...FlightsLoyaltyPointsOption
        }
        partnerLoyaltyEarnAward {
            ...FlightsMarkAndLabel
        }
        formattedPrice {
            __typename
            completeText
            items {
            text
            styles
            }
        }
        formattedMainPrice {
            completeText
            items {
            text
            styles
            }
        }
        identifier
        name
        recommendation {
            ...FlightsBadge
        }
        selected
        showMoreAmenitiesToggle {
            ...FlightsToggleSearch
        }
        totalPrice
        priceAccessibilityMessage
        journeyFareTotalPrice
        upsellOfferToken
        badges {
            accessibility
            text
            theme
        }
        priceLockup {
            accessibilityPrice
            lockupPrice
            strikeThroughPrice
            priceSubtextFirst
        }
        ... on FlightsPMPJourneyFare {
            isPmpSelected
            priceLockupWithPMP {
            accessibilityPrice
            lockupPrice
            strikeThroughPrice
            priceSubtextFirst
            }
            selectFareActionWithPMP {
            ...FlightAction
            }
            priceMatchPromiseSelectionCardSection {
            ...PriceMatchPromiseSelectionCardSectionFragment
            }
            priceMatchPromiseSelectedCardSection {
            ...PriceMatchPromiseSelectedCardSectionFragment
            }
        }
        }
        heading {
        ...FlightsResponsiveMessage
        }
        message
        nextFareChoiceAccessibilityMessage
        previousFareChoiceAccessibilityMessage
        tripTypePerTraveler
        faresTypesLoadingAnalytics {
        faresLoadErrorAnalytics {
            ...FlightsAnalytics
        }
        faresLoadingDisplayedAnalytics {
            ...FlightsAnalytics
        }
        faresLoadingTimeAnalytics {
            ...FlightsAnalytics
        }
        continueButtonOnClickAnalytics {
            ...FlightsAnalytics
        }
        }
        percentageDelaysAndCancellationLink {
        __typename
        analytics {
            ...FlightsAnalytics
        }
        displayAction
        url
        accessibility
        }
        sustainabilityInformation {
        ...FlightsIconPhrases
        }
        dialogs {
        ...FaresDialogsFragment
        }
    }
    flightsJourneyHeaders {
        accessibilityMessage
        flightsJourneySubheadingMark {
        description
        id
        size
        token
        url {
            relativePath
            value
        }
        }
        journeyAmenities {
        ...FlightsJourneyAmenities
        }
        flightsJourneySubheading
        heading
    }
    flightsJourneyInformation {
        ...FlightsJourneyInformation
    }
    flightsJourneyPolicies {
        ...FlightsTextSection
    }
    flightsJourneySummary {
        __typename
        heading {
        __typename
        accessibilityMessage
        text
        }
        differentDayArrival {
        __typename
        accessibilityMessage
        text
        theme
        size
        }
        basicFlightDetails {
        __typename
        accessibilityMessage
        text
        theme
        }
        ... on FlightsBargainJourneySummary {
        arrivalDayInformation
        formattedPrice {
            completeText
            items {
            styles
            text
            }
        }
        tripTypePerTraveler
        totalPrice
        }
    }
    hygieneAmenitiesPresentation {
        __typename
        amenitiesAction {
        __typename
        heading
        onViewedAnalytics {
            ...FlightsAnalytics
        }
        displayAnalyticsList {
            ...FlightsAnalytics
        }
        }
        airlineAmenityGroups {
        __typename
        headerText
        amenities {
            icon {
            ...IconSearch
            }
            label
            theme
        }
        }
        disclaimerMessage
    }
    openAccessibility
    }

    fragment FlightsDetailsAndFaresPresentationFragment on FlightsDetailsAndFaresPresentation {
    __typename
    content {
        ...FlightsDetailsAndFaresContentFragment
    }
    flightsFaresWrapper {
        ...FlightsDialogSheetFragment
    }
    footer {
        ...FlightsDetailsAndFaresFooterFragment
    }
    trigger {
        ...FlightsDialogTriggerFragment
    }
    }

    fragment FlightsDetailsAndFaresContentFragment on FlightsDetailsAndFaresContent {
    __typename
    dialogId
    dynamicDialogId
    nestedDialogs {
        ...FaresDialogsFragment
    }
    priceMatchPromiseNestedDialogs {
        ...FaresDialogsFragment
    }
    sections {
        __typename
        ...FlightsJourneyHeaderFragment
        ...FlightsJourneyDetailsInformationFragment
        ...FlightsJourneyWithDetailsFragment
        ...FlightsHygieneAmenitiesSectionFragment
        ...TextWrapperFragment
        ...FlightsFaresInformationFragment
        ...FlightsSustainabilityCardFragment
        ...FlightsMessagingCardFragment
    }
    }

    fragment FlightsFaresInformationFragment on FlightsFaresInformation {
    __typename
    carousel {
        ...EGDSCarouselContainerFragment
    }
    faresCarousel {
        ...EGDSCarouselFragment
    }
    heading
    fares {
        ...FareInformationCardFragment
    }
    subheading
    scrollAnalytics {
        ...ClientSideAnalytics
    }
    }

    fragment EGDSCarouselFragment on EGDSCarousel {
    nextButton {
        ...EGDSButtonFragment
    }
    previousButton {
        ...EGDSButtonFragment
    }
    }

    fragment FlightsDialogSheetFragment on FlightsDialogSheet {
    __typename
    dialog {
        ...FaresDialogsFragment
    }
    dialogId
    dynamicDialogId
    sheet {
        ...FlightsSideSheetFragment
    }
    }

    fragment FlightsDetailsAndFaresFooterFragment on FlightsDetailsAndFaresFooter {
    __typename
    action {
        ...FlightsActionButton
    }
    dialogId
    dynamicDialogId
    priceLockup {
        ...PriceLockupFragment
    }
    }

    fragment FlightsJourneyHeaderFragment on FlightsJourneyHeaderInformation {
    __typename
    content {
        ...FlightsInformationTextFragment
    }
    }

    fragment FlightsJourneyDetailsInformationFragment on FlightsJourneyDetailsInformation {
    __typename
    content {
        ...FlightsJourneyDetailsFragment
    }
    expando {
        ...EGDSExpandoFragment
    }
    }

    fragment FlightsJourneyDetailsFragment on FlightsJourneyDetails {
    __typename
    journeySections {
        ...JourneySectionFragment
    }
    journeyAmenities {
        ...FlightsIconAndLabel
    }
    }

    fragment FlightsJourneyWithDetailsFragment on FlightsJourneyWithDetails {
    __typename
    details {
        ...EgdsTextFragment
    }
    footnotes {
        ...EgdsTextFragment
    }
    header
    subheader
    }

    fragment FlightsHygieneAmenitiesSectionFragment on FlightsHygieneAmenitiesSection {
    __typename
    header
    footer
    amenities {
        ...EGDSIconTextFragment
    }
    }

    fragment TextWrapperFragment on TextWrapper {
    textA11yMessage: accessibilityMessage
    text {
        ...EgdsTextFragment
        ...EGDSSpannableTextFragment
        __typename
    }
    __typename
    }

    fragment FlightsSustainabilityCardFragment on FlightsSustainabilityCard {
    __typename
    cardContent {
        text {
        ...FlightsPhrase
        }
        icon {
        ...IconSearch
        }
    }
    }

    fragment FareInformationCardFragment on FareInformationCard {
    __typename
    action {
        ...FareActionFragment
    }
    amenities {
        ...FlightsCategorizedListFragment
    }
    fareDetails {
        ...EgdsTextFragment
    }
    heading {
        ...FareHeadingFragment
    }
    priceMatchPromise {
        ...FarePriceMatchPromisePresentationFragment
    }
    state
    highlighted
    scrollAnalytics {
        ...ClientSideAnalytics
    }
    fareTabs {
        ...EGDSBasicTabsFragment
    }
    sponsoredContent {
        ...FlightsSponsoredUpsellDetails
    }
    }

    fragment EGDSBasicTabsFragment on EGDSBasicTabs {
    egdsElementId
    selectedTabId
    tabs {
        ... on EGDSBasicTab {
        tabId
        label
        accessibility
        clickAnalytics {
            ...ClientSideAnalytics
        }
        }
    }
    }

    fragment FlightsSideSheetFragment on FlightsSideSheet {
    content {
        ...EgdsElementFragment
    }
    footer {
        ...EgdsElementFragment
    }
    title
    __typename
    }

    fragment JourneySectionFragment on JourneySection {
    __typename
    journeyConnectionInformation {
        ... on AdditionalInformation {
        ...AdditionalInformationFragment
        }
        ... on FlightsConnectionInformation {
        ...FlightsConnectionInformationFragment
        }
    }
    }

    fragment EGDSExpandoFragment on EGDSExpando {
    __typename
    ... on EGDSExpandoPeek {
        ...EGDSExpandoPeekFragment
    }
    ... on EGDSExpandoListItem {
        ...EGDSExpandoListItemFragment
    }
    ... on EGDSExpandoLink {
        ...EGDSExpandoLinkFragment
    }
    }

    fragment EGDSIconTextFragment on EGDSIconText {
    __typename
    icon {
        ...IconSearch
    }
    text
    }

    fragment EGDSCarouselContainerFragment on EGDSCarouselContainer {
    __typename
    accessibilityHeadingText
    nextButtonText
    previousButtonText
    }

    fragment FareActionFragment on FareAction {
    __typename
    action {
        ...FlightsActionButton
    }
    states
    }

    fragment FlightsCategorizedListFragment on FlightsCategorizedList {
    __typename
    sections {
        ...FlightsCategorizedListSectionFragment
    }
    }

    fragment FlightsCategorizedListSectionFragment on FlightsCategorizedListSection {
    __typename
    flightsCategorizedListSectionA11yMessage: accessibilityMessage
    footnote
    heading
    additionalInfo
    items {
        ...FlightsCategorizedListItemFragment
    }
    }

    fragment FlightsCategorizedListItemFragment on FlightsCategorizedListItem {
    __typename
    primary {
        ...EGDSSpannableTextFragment
    }
    secondary
    tertiary
    }

    fragment FareHeadingFragment on FareHeading {
    __typename
    badge {
        ...EGDSBadgeFragment
    }
    farePricing {
        ...FarePricingFragment
    }
    }

    fragment FarePriceMatchPromisePresentationFragment on FarePriceMatchPromisePresentation {
    __typename
    cards {
        ...FarePriceMatchPromiseSelectableCardFragment
        ...FarePriceMatchPromiseRemovableCardFragment
        ...FarePriceMatchPromiseStaticCardFragment
    }
    priceMatchPromiseState
    }

    fragment FarePriceMatchPromiseStaticCardFragment on FarePriceMatchPromiseStaticCard {
    __typename
    heading {
        ...EGDSIconTextFragment
    }
    priceMatchPromiseState
    subHeading
    }

    fragment FarePriceMatchPromiseRemovableCardFragment on FarePriceMatchPromiseRemovableCard {
    __typename
    heading {
        ...EGDSIconTextFragment
    }
    priceMatchPromiseState
    removeAction {
        ...FlightsActionLinkFragment
    }
    subHeading
    }

    fragment AdditionalInformationFragment on AdditionalInformation {
    __typename
    durationAndStop
    nextFlightOriginAirportInfo {
        ...FlightsIconAndLabel
    }
    }

    fragment FlightsConnectionInformationFragment on FlightsConnectionInformation {
    __typename
    flightsConnection {
        aircraftModel
        airlineInfo
        cabinClassAndBookingCode
        connectionArrival {
        ...CoordinateInformationSearch
        }
        connectionDeparture {
        ...CoordinateInformationSearch
        }
        duration
        journeyAmenities {
        ...FlightsJourneyAmenities
        }
    }
    }

    fragment EGDSExpandoPeekFragment on EGDSExpandoPeek {
    __typename
    expandedLabel
    collapsedLabel
    expandAnalytics {
        ...ClientSideAnalytics
    }
    threshold
    minimalHeight
    }

    fragment EGDSExpandoListItemFragment on EGDSExpandoListItem {
    __typename
    collapseAnalytics {
        ...ClientSideAnalytics
    }
    collapsedLabel
    expandAnalytics {
        ...ClientSideAnalytics
    }
    expandedLabel
    expanded
    }

    fragment EGDSExpandoLinkFragment on EGDSExpandoLink {
    __typename
    collapseAnalytics {
        ...ClientSideAnalytics
    }
    collapsedLabel
    expandAnalytics {
        ...ClientSideAnalytics
    }
    expanded
    expandedLabel
    }

    fragment FlightsInformationTextFragment on FlightsInformationText {
    __typename
    content {
        ...FlightsInformationTextItemFragment
    }
    }

    fragment FlightsInformationTextItemFragment on FlightsInformationTextItem {
    ...MarkWrapperFragment
    ...TextWrapperFragment
    ...IconWrapperFragment
    ...SuperlativeTextFragment
    }

    fragment EGDSBadgeFragment on EGDSBadge {
    __typename
    accessibility
    text
    theme
    }

    fragment FarePricingFragment on FarePricing {
    __typename
    priceLockup {
        ...PriceLockupFragment
    }
    states
    }

    fragment FarePriceMatchPromiseSelectableCardFragment on FarePriceMatchPromiseSelectableCard {
    __typename
    checkbox {
        ...FlightsActionCheckboxFragment
    }
    heading {
        ...EGDSIconTextFragment
    }
    infoTrigger {
        ...FlightsDialogTriggerFragment
    }
    price
    priceMatchPromiseState
    description
    }

    fragment EGDSSpannableTextFragment on EGDSSpannableText {
    __typename
    text
    contents {
        __typename
        ...EgdsTextFragment
    }
    inlineContent {
        __typename
        ...EgdsTextFragment
    }
    }

    fragment MarkWrapperFragment on MarkWrapper {
    __typename
    mark {
        ...MarkFragments
    }
    }

    fragment IconWrapperFragment on IconWrapper {
    __typename
    iconA11yMessage: accessibilityMessage
    icons {
        ...IconSearch
    }
    }

    fragment MarkFragments on Mark {
    __typename
    description
    id
    markSize: size
    url {
        ... on HttpURI {
        __typename
        relativePath
        value
        }
    }
    }

    fragment SuperlativeTextFragment on SuperlativeText {
    __typename
    superlativeTextA11yMessage: accessibilityMessage
    text {
        ...EgdsTextFragment
    }
    }

    fragment FlightsJourneyAmenities on FlightsJourneyAmenities {
    __typename
    accessibilityMessage
    amenities {
        ...FlightsIconAndLabel
    }
    analytics {
        ...FlightsAnalytics
    }
    }

    fragment FlightsJourneyAmenitiesWithLabel on FlightsJourneyAmenitiesWithLabel {
    __typename
    label
    rules {
        ...FlightsJourneyAmenities
    }
    }

    fragment Pagination on Pagination {
    __typename
    size
    startingIndex
    }

    fragment FlightsIconAndLabel on FlightsIconAndLabel {
    __typename
    icon {
        ...IconSearch
    }
    label
    subLabel
    accessibility
    value
    theme
    displayAnalytics {
        ...FlightsAnalytics
    }
    }

    fragment FlightsJourneyInformation on FlightsDetailedJourneyInformation {
    __typename
    details {
        ...FlightsToggleSearch
    }
    flightJourneyDetails {
        __typename
        journeySections {
        journeyConnectionInformation {
            __typename
            ... on AdditionalInformation {
            durationAndStop
            nextFlightOriginAirportInfo {
                ...FlightsIconAndLabel
            }
            }
            ... on FlightsConnectionInformation {
            flightsConnection {
                aircraftModel
                airlineInfo
                cabinClassAndBookingCode
                connectionArrival {
                ...CoordinateInformationSearch
                }
                connectionDeparture {
                ...CoordinateInformationSearch
                }
                duration
                journeyAmenities {
                ...FlightsJourneyAmenities
                }
                operatedBy
            }
            }
        }
        }
        journeyAmenities {
        ...FlightsIconAndLabel
        }
    }
    }

    fragment FlightsBadge on FlightsBadge {
    __typename
    accessibilityMessage
    icon {
        id
        description
    }
    text
    type
    }

    fragment HotelsDate on FlightsSearchFormDateField {
    __typename
    analytics {
        ...FlightsAnalytics
    }
    currentError
    date {
        day
        month
        year
        formatted(format: \"d MMM uuuu\")
        isoFormat
    }
    dateFormat
    daysBookableInAdvance
    label
    placeholder
    possibleErrors {
        analytics {
        ...FlightsAnalytics
        }
        message
        type
    }
    maxStayDurationAllowed
    possibleErrorsHeader {
        icon {
        id
        description
        }
        label {
        completeText
        items {
            styles
            text
        }
        }
    }
    doneAction
    }

    fragment ClientMetaData on FlightsPWAMetadata {
    pageName
    pageNameAnalytics {
        ...FlightsAnalytics
    }
    responseTags
    }

    fragment FlightsRewardsPricingInfo on FlightsRewardsPricingInfo {
    title {
        ...FlightsResponsiveMessage
    }
    options {
        ... on FlightsRewardsOption {
        label
        identifier
        selected
        accessibility {
            ... on FlightsAccessibilityMessage {
            usage
            onCompletion
            }
        }
        }
    }
    subText {
        completeText
        delimeter
        items {
        __typename
        styles
        text
        ... on FlightsPhraseLinkNode {
            accessibility
            analytics {
            ...FlightsAnalytics
            }
            icon
            link
        }
        ... on FlightsPhraseDialogNode {
            dialog {
            __typename
            title
            message
            animation
            actions {
                ...FlightAction
            }
            displayedAnalytics {
                ...FlightsAnalytics
            }
            }
            actionableIcon {
            ... on Icon {
                id
                description
                token
            }
            }
        }
        }
    }
    loyaltyBanners {
        ...FlightsIconPlacard
    }
    }

    fragment PageTitle on FlightsPageTitle {
    date {
        longMessage
        shortMessage
    }
    disclaimerSubTitle {
        ...FlightsPhrase
    }
    title {
        longMessage
        shortMessage
    }
    }

    fragment FlightsActionableIcon on FlightsActionableIcon {
    __typename
    icon {
        ...IconSearch
    }
    analytics {
        ...FlightsAnalytics
    }
    type
    }

    fragment FlightsResponsiveMessage on FlightsResponsiveMessage {
    __typename
    longMessage
    shortMessage
    }

    fragment FlightsPhrase on FlightsPhrase {
    completeText
    delimeter
    theme
    items {
        __typename
        text
        styles
        ... on FlightsPhraseLinkNode {
        accessibility
        analytics {
            ...FlightsAnalytics
        }
        displayAnalytics {
            ...FlightsAnalytics
        }
        scrollAnalytics {
            ...FlightsAnalytics
        }
        link
        icon
        }
        ... on FlightsPhraseDialogNode {
        accessibility
        analytics {
            ...FlightsAnalytics
        }
        actionableIcon {
            id
            description
        }
        dialog {
            __typename
            title
            message
            animation
            actions {
            ...FlightAction
            }
            displayedAnalytics {
            ...FlightsAnalytics
            }
        }
        }
    }
    }

    fragment FlightsIconPhrases on FlightsIconPhrases {
    text {
        ...FlightsPhrase
    }
    icon {
        ...IconSearch
    }
    }

    fragment AlternateAirportOptions on AlternateAirportOptions {
    accessibilityTitle
    airportOptionAnalytics {
        ...FlightsAnalytics
    }
    airportOptions {
        ...AirportOption
    }
    alternateOptionTitle
    }

    fragment AirportOption on AirportOption {
    accessibilityHeading
    accessibilityMessage
    destinationAirportDistance
    destinationCityName
    icon {
        ...IconSearch
    }
    originAirportDistance
    originCityName
    selectAction {
        ...FlightAction
    }
    }

    fragment AlternateDateOptions on AlternateDateOptions {
    accessibilityTitle
    dateOptionAnalytics {
        ...FlightsAnalytics
    }
    dateOptions {
        ...DateOption
    }
    alternateOptionTitle
    }

    fragment DateOption on DateOption {
    accessibilityHeading
    accessibilityMessage
    numDaysDifference
    selectAction {
        ...FlightAction
    }
    tripDates
    tripOD
    }

    fragment FlightsDisplayComponentCountingValue on FlightsDisplayComponentCountingValue {
    displayCount
    flightsDisplayComponent
    }

    fragment DateFragment on Date {
    month
    day
    year
    }

    fragment MultiItemPackageableProduct on MultiItemPackageableProduct {
    flights {
        offerToken
        productTokens
        travelers {
        age
        type
        }
    }
    }

    fragment MultiItemFlightCrossSellPrimer on MultiItemFlightCrossSellPrimer {
    __typename
    flightCrossSellProductType
    multiItemSearchContext {
        ...MultiItemSearchContext
    }
    }

    fragment FlightsCrossSellOffer on FlightsCrossSellOffer {
    multiItemFlightCrossSellOfferPrimer {
        multiItemSearchContext {
        ...MultiItemSearchContext
        }
        multiItemPackageableProduct {
        ...MultiItemPackageableProduct
        }
        brandedDealFallBack {
        ...MultiItemFlightCrossSellPrimer
        }
        price {
        base {
            amount
        }
        taxesAndFees {
            amount
        }
        }
    }
    }

    fragment FlightsFiltersEventAnalytics on FlightsFiltersEventAnalytics {
    filterAppliedEventName
    filterRemovedEventName
    eventType
    eventCategory
    pageName
    }

    fragment FlightsFilterItemAnalytics on FlightsFilterItemAnalytics {
    id
    position
    category
    value
    min
    max
    }

    fragment FlightsOfferNaturalKeysFragment on FlightsOfferNaturalKeys {
    flightNaturalKey {
        offerToken
        productTokens
        travelers {
        age
        type
        }
    }
    packagedProductsNaturalKeys {
        __typename
        ... on CarNaturalKey {
        __typename
        offerToken
        }
        ... on PropertyNaturalKey {
        __typename
        id
        ratePlanId
        roomTypeId
        inventoryType
        checkOut {
            ...DateFragment
        }
        checkIn {
            ...DateFragment
        }
        rooms {
            childAges
            numberOfAdults
        }
        }
    }
    }

    fragment PriceLockupFragment on EGDSPriceLockup {
    accessibilityPrice
    leadingCaption
    lockupFormattedPoints
    lockupPrice
    priceSubtextFirst
    priceSubtextBold
    priceSubtextStandard
    strikeThroughPrice
    }

    fragment FlightsMessagingCardPlacardFragment on FlightsMessagingCardPlacard {
    messagingCard {
        ...UIMessagingCard
    }
    button {
        primary
        clientAction {
        ...ClientActionFragment
        }
    }
    onViewedAnalytics {
        ...FlightsAnalytics
    }
    onViewedAnalyticsList {
        ...ClientSideAnalytics
    }
    actionElement {
        ...FlightsClientActionElement
    }
    }

    fragment FlightsClientActionElement on FlightsClientActionElement {
    ...FlightsActionLinkFragment
    }

    fragment EgdsGraphicIllustrationFragmentSearch on Illustration {
    link: url
    id
    description
    egdsElementId
    }

    fragment ClientActionFragment on FlightsDialogTriggerAction {
    dialog {
        ...EGDSFullScreenDialogFragment
    }
    dialogContents {
        ...EgdsElementFragment
    }
    analyticsList {
        __typename
        ...ClientSideAnalytics
    }
    }

    fragment EGDSFullScreenDialogFragment on EGDSFullScreenDialog {
    ... on EGDSFullScreenDialog {
        toolbar {
        ...EGDSDialogToolbarFragment
        }
    }
    }

    fragment EGDSButtonFragment on EGDSButton {
    __typename
    ...FlightsActionButton
    ...FlightsDialogTriggerFragment
    }

    fragment FlightsDialogTriggerFragment on FlightsDialogTrigger {
    __typename
    dialogAction
    dialogId
    dynamicDialogId
    trigger {
        __typename
        ...FlightsActionButton
        ...FlightsActionLinkFragment
        ...FlightsExperienceActionButtonFragment
        ...FlightsExperienceActionLinkFragment
    }
    }

    fragment FlightsExperienceActionButtonFragment on FlightsExperienceActionButton {
    __typename
    accessibility
    clientAction {
        __typename
        accessibility
        analyticsList {
        ...ClientSideAnalytics
        }
        ...FlightsSelectionAction
    }
    primary
    }

    fragment FlightsExperienceActionLinkFragment on FlightsExperienceActionLink {
    __typename
    accessibility
    clientAction {
        __typename
        accessibility
        analyticsList {
        ...ClientSideAnalytics
        }
        ...FlightsSelectionAction
    }
    primary
    }

    fragment EGDSDialogToolbarFragment on EGDSDialogToolbar {
    title
    closeText
    }

    fragment EgdsElementFragment on EGDSElement {
    __typename
    ... on EGDSText {
        ...EgdsTextFragment
    }
    ... on Illustration {
        ...EgdsGraphicIllustrationFragmentSearch
    }
    ... on UIMessagingCard {
        primary
        secondaries
        graphic {
        __typename
        ... on Illustration {
            link: url
        }
        ...EgdsGraphicIllustrationFragmentSearch
        }
    }
    ... on EGDSBulletedList {
        listItems {
        __typename
        text
        }
    }
    }

    fragment EgdsTextFragment on EGDSText {
    __typename
    ... on EGDSHeading {
        text
        headingType
    }
    ... on EGDSParagraph {
        text
        style
    }
    ... on EGDSIconText {
        text
        icon {
        id
        size
        }
    }
    ... on EGDSStandardLink {
        text
        action {
        __typename
        accessibility
        target
        resource {
            __typename
            value
        }
        analytics {
            __typename
            linkName
            referrerId
        }
        }
    }
    ... on EGDSPlainText {
        text
    }
    ... on EGDSStylizedText {
        text
        theme
        weight
    }
    }

    fragment FaresDialogsFragment on FlightsDialog {
    dialog {
        __typename
        ...EGDSDialogFragment
    }
    dialogContent: content {
        __typename
        ...EgdsElementFragment
        ... on FlightsDialogTrigger {
        ...FlightsDialogTriggerFragment
        }
    }
    dialogId
    dynamicDialogId
    }

    fragment EGDSDialogFragment on EGDSDialog {
    closeAnalytics {
        ...ClientSideAnalytics
    }
    ...EGDSFullScreenDialogFragment
    ... on EGDSActionDialog {
        __typename
        footer {
        __typename
        buttons {
            ...EGDSButtonFragment
        }
        }
    }
    }

    fragment PriceMatchPromiseSelectionCardSectionFragment on PriceMatchPromiseSelectionCardSection {
    header
    description
    price
    icon {
        ...IconSearch
    }
    toggleCheckbox {
        ...FlightsActionCheckboxFragment
    }
    infoTrigger {
        ...FlightsDialogTriggerFragment
    }
    onDisplayAnalytics {
        ...FlightsAnalytics
    }
    }

    fragment PriceMatchPromiseSelectedCardSectionFragment on PriceMatchPromiseSelectedCardSection {
    header
    description
    icon {
        ...IconSearch
    }
    removeActionLink {
        ...FlightsActionLinkFragment
    }
    onDisplayAnalytics {
        ...FlightsAnalytics
    }
    }

    fragment FlightsActionCheckboxFragment on FlightsActionCheckbox {
    label {
        ...EgdsTextFragment
    }
    clientAction {
        ...FlightsClickActionFragment
    }
    }

    fragment FlightsActionLinkFragment on FlightsActionLink {
    __typename
    clientAction {
        ...FlightsClientActionFragment
    }
    disabled
    primary
    icon {
        ...IconSearch
    }
    analytics {
        ...ClientSideAnalytics
    }
    }

    fragment FlightsClientActionFragment on FlightsClientAction {
    accessibility
    analyticsList {
        ...ClientSideAnalytics
    }
    ... on FlightsCreditSelectionAction {
        originalBookingId
    }
    ...FlightsBoundNavigation
    ...FlightsNavigateToDetails
    ...FlightsResourceLinkAction
    ...FlightsSelectionAction
    ...MultiItemSelectPackage
    ...MultiItemSelectProducts
    }

    fragment FlightsClickActionFragment on FlightsClickAction {
    __typename
    analyticsList {
        __typename
        ...ClientSideAnalytics
    }
    accessibility
    }

    fragment FlightsMessagingCardFragment on FlightsMessagingCard {
    cardContent {
        ...EGDSStandardMessagingCardFragment
    }
    displayAnalytics {
        ...ClientSideAnalytics
    }
    }

    fragment EGDSStandardMessagingCardFragment on EGDSStandardMessagingCard {
    dismiss {
        ...EGDSDismissActionFragment
    }
    egdsElementId
    graphic {
        ...UIGraphicFragment
    }
    heading
    links {
        ...EGDSStandardLinkFragment
    }
    message
    rightIcon {
        ...IconSearch
    }
    }

    fragment EGDSDismissActionFragment on EGDSDismissAction {
    accessibility
    analytics {
        ...ClientSideAnalytics
    }
    label
    }

    fragment UIGraphicFragment on UIGraphic {
    ...IconSearch
    ...MarkFragments
    ...EgdsGraphicIllustrationFragmentSearch
    }

    fragment EGDSStandardLinkFragment on EGDSStandardLink {
    action {
        ...UILinkActionFragment
    }
    disabled
    icon {
        ...IconSearch
    }
    iconPosition
    size
    text
    }

    fragment UILinkActionFragment on UILinkAction {
    accessibility
    analytics {
        ...ClientSideAnalytics
    }
    resource {
        value
    }
    target
    useRelativePath
    }

    fragment FlightsListingMessagingCard on FlightsListingMessagingCard {
    messagingCard {
        ...FlightsMessagingCardPlacardFragment
    }
    }

    fragment FlightsOfferSponsoredUpsell on FlightsOfferSponsoredUpsell {
    __typename
    badge {
        ...EGDSBadgeFragment
    }
    expando {
        ...EGDSExpandoFragment
    }
    details {
        ...FlightsSponsoredUpsellDetails
    }
    action {
        ...FlightsDialogTriggerFragment
    }
    onViewedAnalytics {
        ...ClientSideAnalytics
    }
    sponsoredFareAnalyticsList {
        ...ClientSideAnalytics
    }
    }

    fragment FlightsSponsoredUpsellDetails on FlightsSponsoredFareInformation {
    __typename
    mediaSection {
        badge {
        ...EGDSBadgeFragment
        }
        featureImage {
        url
        description
        thumbnailClickAnalytics {
            ...ClientSideAnalytics
        }
        }
    }
    heading {
        __typename
        accessibility
        text
    }
    description
    bulletpoints {
        __typename
        listItems {
        __typename
        text
        }
    }
    priceLockup {
        ...PriceLockupFragment
    }
    }
    """,
        "variables": {
            "context": {
                "siteId": 80001,
                "locale": "en_US",
                "eapid": 0,
                "currency": "USD",
                "device": {"type": "DESKTOP"},
                "identity": {
                    "duaid": "ae80c705-d736-4803-81a9-20f3d6e0e2ae",
                    "expUserId": "-1",
                    "tuid": "-1",
                    "authState": "ANONYMOUS"
                },
                "privacyTrackingState": "CAN_TRACK",
                "debugContext": {
                    "abacusOverrides": [],
                    "alterMode": "RELEASED"
                }
            },
            "flightsSearchContext": {
                "tripType": "ONE_WAY",
                "journeysContinuationId": None,
                "originalBookingId": None
            },
            "journeyCriteria": [
                {
                    "departureDate": {
                        "month": month,
                        "day": day,
                        "year": year
                    },
                    "destination": dest,
                    "origin": orig
                }
            ],
            "queryState": "LOADED",
            "searchFilterValuesList": [{"preferredAirlineFilterValue": {"carrierCode": "NK"}}],
            "searchPreferences": {
                "advancedFilters": [],
                "airline": "*",
                "cabinClass": "COACH"
            },
            "sortOption": {
                "sortOrder": "INCREASING",
                "sortType": "BEST_BETS"
            },
            "travelerDetails": [
                {
                    "travelerType": "ADULT",
                    "count": 1
                }
            ],
            "searchPagination": {
                "size": 5,
                "startingIndex": 0
            },
            "flightsSearchComponentCriteria": None,
            "shoppingContext": None,
            "virtualAgentContext": None,
            "faresSeparationType": "BASE_AND_UPSELL"
        }
    }
    headers = {
        "cookie": "linfo=v.4,|0|0|255|1|0||||||||1033|0|0||0|0|0|-1|-1; CRQSS=e|0; CRQS=t|80001`s|80001`l|en_US`c|USD; currency=USD; iEAPID=0; tpid=v.1,80001; HMS=1df64868-7d2e-4912-b165-cf0b7e28c1a8; MC1=GUID=ae80c705d736480381a920f3d6e0e2ae; DUAID=ae80c705-d736-4803-81a9-20f3d6e0e2ae; _abck=1837FE33C7AC000A4CF58C34995091F5~-1~YAAQTo9lXzlJdheGAQAAYABTJQmvU8QywOC5PxdCs/LESg0/JxUaLkHk0zF3Jeq4+PBzC3ZPhYA6JobZPDC5kc91iY/NxeRbULNfC3azwMF+zcj848wg+jnILlqTj+4wghfQd7kJ8HrbE5INZk4QMuiMDnSYy2/+slylFcvXzKFVh/7bNgnLAvyllSTJxwf/YcN8YdoDxkm+3cCFOKiskgE4cHYVBO0rjSGhe4p81GDmwIL+/aqynOO7MMGtl3pVvaweAaORv86IYdLXuDB9AKwuPl5DSjaCx78WR7YXuzPbpJPG9TEUyUPIsvrYiPmEC9NAnBw2Are5FECORKM0Ik7KPDh2HK1kGCNgLBvISU4jRUoIcdGwj0LWP0ui69IB9Q==~-1~-1~-1; bm_sz=0C34457EF434BEB16810B7BBB838D1C2~YAAQTo9lXzxJdheGAQAAYABTJRKz1suPXhVJfc7o+dz6lw8Vmaj+YnVdBeKI2Ny3EoCdRIQCb3onn9l6cHn/7qG94kaJNrmSygsYvbbyQdM0PPz7zGwqB2OGpAYe0yLS73y/EHpc52agId/nwuHX7Gf3y92DYgZOqhHryPIDU94LoQPKOn43p5qzUSxRe9YjWhgy+JZIkmalBfxedItjnskEqCkz+aJ73QOxylkHLNfQmJQjP4swxdVSE4V4j1Jrhr6cOPPXmqdK7zJEbpj54y0meiEKCXDmUKXZYjio7QeYif6b1zQbyQ==~4469559~3355717; bm_mi=E0FB1B340E930A0B87F68F2AC02AC7EE~YAAQTo9lXyxMdheGAQAAEh5TJRK0LR6/nL4Plp8dC3Rqdb4BkUxhdmLh2ShZv7C9AycmEUSgby7ofb8yVDEsJs01gTKx16N7FIBH4vv5yPpYp8KW6apzJqIKULPH7Cvngdxu06Di5yfgP6ZdbYArl3G53CzjfevlmjRf/NWTMzj8LNoKZPFEAebnv/YezBcv7R0aFlo77pCPIP3a2ScKezGL7VZQPgSQ6XVSzDNVK8Eu1a+DFgz+pkFel2hqIfIpGttuEe4GP2EAqg5Y+CD9KFip6bVKtm0Tg5ZPh/jLw8/b6Qfd7EJM94KqYUVwFgoDfUDL~1; ak_bmsc=872B8F157E3B5FB74CCBFE6ED25C72FF~000000000000000000000000000000~YAAQTo9lX9dSdheGAQAAMlJTJRLxo9LFKmBXSyJYfEV+KGVJIzmBayQhKqhp+JwpfuGMVfXGRt0xz8bjemsk0PPQaYF4ca2Ti3md5Nkm2WXx/xJwcXpq4uuDjIpRmM16vNKD/N3E62fIWH7l9X0yTP8v3ti+2sKAM/lwcKsRaN9iVFKK0u98sz/oXHqs/zUAObFsPly/RMeorGhGjyxT1r96jVF18uCWmX00qewskzCeK5rIeL6CWEffHSRdQa2kjjoPhjiigLmYDETY4zqDMRSNSVq2cZzBB7B9LPYAbjTFrW424bYKjeew/3dARQB65+/wPaCZwJRbILElbqLjrxW7j/rpHQPtVKHoFu8IEAGqtMRbiXy1NBUULDKwyQ16b9uINirEkLLm7N1Mw5zWsffYCbmnmNLHQIx8Qj6TbnTWSJrm9kIvH1wBe0rBkeeS4SHlsTx0Xk7S4vp4IRDnRdxQWgocRsmLYkGiYstiMKdKgLoBohl3LpzTfRcelhI8wiTxgiwDoCQ=; s_ppv=%5B%5BB%5D%5D; s_ips=1; AMCVS_C00802BE5330A8350A490D4C%40AdobeOrg=1; s_cc=true; session_id=1df64868-7d2e-4912-b165-cf0b7e28c1a8; _fbp=fb.1.1675663626181.784000829; xdid=1e131285-7a3c-4683-9f86-b1faf678456f|1675663648|travelocity.com; eg_ppid=3ccdfcb4-f0cd-474e-981e-e149b428f7e1; __gads=ID=0ed1c281f4e446b2:T=1675663676:S=ALNI_MZ2ctcTA7HoRelF82ipmdeolBBvWQ; __gpi=UID=00000bd457b0c301:T=1675663676:RT=1675663676:S=ALNI_Mbf12Vt1FOnJSQXPDJrO_12SBkyOg; _gcl_au=1.1.725592271.1675663820; x-cgp-pwa-flight-rolled-pos=40384.PWA; s_ppn=page.Flight-Search-Oneway; page_name=page.Flight-Search-Oneway; AMCV_C00802BE5330A8350A490D4C%40AdobeOrg=1585540135%7CMCIDTS%7C19395%7CMCMID%7C88314170025306873463954463791256176062%7CMCAAMLH-1676268850%7C6%7CMCAAMB-1676268850%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1675671250s%7CNONE%7CvVersion%7C4.4.0%7CMCAID%7CNONE%7CMCCIDH%7C-2034012538; s_tp=967; _uetsid=75439b50a5e411ed992a214a17fa3f54; _uetvid=75442fe0a5e411edb19481766e49dd3c; JSESSIONID=F1BCCC025BE56D48369447585180542C; AWSALB=Zgn/xHk0N3G2a3tSvWdNV3ng7hmw5SozOu0WxB+stQUVYZxIcWuReKL5FIDK56B7yXqlkOKHOIoLz/2W4+JUmAKz4lJyqAt55Vb7wr5aRZme4VUCAPYUBjcvzQK8; AWSALBCORS=Zgn/xHk0N3G2a3tSvWdNV3ng7hmw5SozOu0WxB+stQUVYZxIcWuReKL5FIDK56B7yXqlkOKHOIoLz/2W4+JUmAKz4lJyqAt55Vb7wr5aRZme4VUCAPYUBjcvzQK8; cesc=%7B%22marketingClick%22%3A%5B%22false%22%2C1675667823909%5D%2C%22hitNumber%22%3A%5B%2241%22%2C1675667823908%5D%2C%22visitNumber%22%3A%5B%221%22%2C1675663442008%5D%2C%22cidVisit%22%3A%5B%22SEO.B.google.com%22%2C1675667823909%5D%2C%22entryPage%22%3A%5B%22Homepage%22%2C1675667823908%5D%2C%22seo%22%3A%5B%22SEO.B.google.com%22%2C1675663442008%5D%2C%22cid%22%3A%5B%22SEO.B.google.com%22%2C1675663442008%5D%7D; bm_sv=F5CF589816F67981D0876861E64C953C~YAAQTo9lX8cdfReGAQAAWt2VJRIgWVCf0UufPwF5R+4ft1PlK3iluFFThssOfzP1RrA5N2kWZsccrouQUbvQb75NGNE6pZAdiLr5cGe07UBiQx7/0jGQIEdf8JXvEMm5SnmmFkfAO7JVhoX4lg/7UZVtw1eOQeIxd2GCuSRrOYxypPUQGh29O0JH0HD2+179tptLqjSooqWMrqPpZLkuwMiK9og9dI89suWRGljBRpS8JTmh8eWims57ocqolil7uL5Atz5S~1",
        "authority": "www.travelocity.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "client-info": "flights-shopping-pwa,latest,us-east-1",
        "content-type": "application/json",
        "credentials": "same-origin",
        "device-user-agent-id": "ae80c705-d736-4803-81a9-20f3d6e0e2ae",
        "origin": "https://www.travelocity.com",
        "referer": "https://www.travelocity.com/Flights-Search?filters=%5B%7B%22preferredAirlineFilterValue%22%3A%7B%22carrierCode%22%3A%22NK%22%7D%7D%5D&leg1=from%3ASeattle%2C%20WA%20%28SEA-Seattle%20-%20Tacoma%20Intl.%29%2Cto%3ALas%20Vegas%2C%20NV%20%28LAS-Harry%20Reid%20Intl.%29%2Cdeparture%3A2%2F11%2F2023TANYT&mode=search&options=carrier%3A%2A%2Ccabinclass%3A%2Cmaxhops%3A1%2Cnopenalty%3AN&passengers=adults%3A1%2Cchildren%3A0%2Cinfantinlap%3AN&sortOrder=INCREASING&sortType=BEST_BETS&trip=oneway",
        "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "x-page-id": "page.Flight-Search-Oneway,F,20"
    }


    for y in range(7):
        y = y + 1
        print(f'Date {y}')
        response = requests.request("POST", url, json=payload, headers=headers)
        data = response.json()

        for x in (data['data']['flightsSearch']['listingResult']['listings'][1:]):
            date = data['extensions']['analytics'][0]['adobeMappedData']['prop5']
            dep_arriv_time = x['journeys'][0]['departureAndArrivalTime']['completeText'].split('-')
            Tdeparture = dep_arriv_time[0]
            Tarrival = dep_arriv_time[1]

            dep_arriv_loc = x['journeys'][0]['departureAndArrivalLocations'].split('-')
            Ldeparture = dep_arriv_loc[0]
            Larrival = dep_arriv_loc[1]

            item = {
                'Flight ID': x['journeys'][0]['flightsDetailsAndFaresPresentation']['content']['sections'][1]['content'][0]['journeySections'][0]['journeyConnectionInformation'][0]['flightsConnection']['airlineInfo'],
                'Duration': x['journeys'][0]['flightsDetailsAndFaresPresentation']['content']['sections'][1]['content'][0]['journeySections'][0]['journeyConnectionInformation'][0]['flightsConnection']['duration'],
                'Price': x['journeys'][0]['flightsDetailsAndFaresPresentation']['content']['sections'][2]['fares'][0]['heading']['farePricing'][0]['priceLockup']['lockupPrice'],
                'Depart Time': Tdeparture,
                'Depart Location': Ldeparture,
                'Arrival Time': Tarrival,
                'Arrival Location': Larrival,
                'Date': date
            }

            item_list.append(item)
        payload['variables']['journeyCriteria'][0]['departureDate']['day'] += 1


    json_str = json.loads(json.dumps(item_list, indent=None))
    return json_str